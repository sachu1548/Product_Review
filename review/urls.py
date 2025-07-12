from django.urls import path
from . import views
from .views import custom_logout_view

urlpatterns = [
    path('register/', views.RegisterUserView.as_view(), name='register'),
    path('products/', views.ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', views.ProductRetrieveUpdateDestroyView.as_view(), name='product-detail'),
    path('products/<int:product_id>/reviews/', views.ReviewListCreateView.as_view(), name='product-reviews'),
    path('logout/', custom_logout_view, name='logout'),
]
