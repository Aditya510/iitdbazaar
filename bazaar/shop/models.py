from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    content = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    date_posted = models.DateTimeField(default=timezone.now)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    available = models.BooleanField(default=True)
    image = models.ImageField(default='defaultproduct.jpg', upload_to='profile_pics')



    def __str__(self):
        return self.title

