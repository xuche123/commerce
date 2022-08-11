from tkinter import CASCADE
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    title = models.CharField(max_length=64)
    desc = models.TextField()
    image = models.ImageField(blank=True, upload_to='')

    category = models.CharField(max_length=64)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sales")
    time_created = models.DateTimeField(auto_now_add=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    starting_price = models.DecimalField(max_digits=12, decimal_places=2)

class Comment(models.Model):
    content = models.TextField()
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    time = models.DateTimeField(auto_now_add=True)

class Bids(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bids")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids")
    price = models.DecimalField(max_digits=12,decimal_places=2)