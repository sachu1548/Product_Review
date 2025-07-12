
from django.contrib.auth import logout
from django.shortcuts import redirect
from rest_framework import generics, permissions, serializers
from django.db.models import Avg
from .models import Product, Review
from .serializers import ProductSerializer, ReviewSerializer, UserSerializer
from .permissions import IsAdminUserOrReadOnly
from django.contrib.auth.models import User

class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all().annotate(average_rating=Avg('reviews__rating'))
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all().annotate(average_rating=Avg('reviews__rating'))
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class ReviewListCreateView(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs['product_id'])

    def perform_create(self, serializer):
        product_id = self.kwargs['product_id']
        user = self.request.user
        if Review.objects.filter(product_id=product_id, user=user).exists():
            raise serializers.ValidationError("You have already reviewed this product.")
        serializer.save(user=user, product_id=product_id)



def custom_logout_view(request):
    logout(request)
    return redirect('/api-auth/login/')
