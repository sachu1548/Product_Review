from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products',null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def average_rating(self):
        return self.reviews.aggregate(models.Avg('rating'))['rating__avg'] or 0

    def __str__(self):
        return self.name

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    feedback = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ['product', 'user']

    def __str__(self):
        return f"{self.user.username} - {self.product.name} ({self.rating})"
