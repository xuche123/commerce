from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class Listing(models.Model):
    CATEGORIES = [
        ('TOYSANDGAMES', 'Toys and Games'),
        ('ELECTRONICS', 'Electronics'),
        ('APPAREL', 'Apparel'),
        ('HOMEAPPLIANCES', 'Home Appliances'),
        ('BEAUTY', 'Beauty'),
        ('HOUSEHOLDPRODUCTS', 'Household Products'),
        ('FUNITURE', 'Furniture'),
        ('GROCERIES', 'Groceries')
    ]
    title = models.CharField(max_length=64)
    desc = models.TextField()
    image_url = models.URLField(blank=True)
    image = models.ImageField(upload_to="", null= True, blank=True)

    category = models.CharField(max_length=32, choices=CATEGORIES, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sales")
    time_created = models.DateTimeField(auto_now_add=True)
    # start_time = models.DateTimeField()
    # end_time = models.DateTimeField()
    starting_price = models.DecimalField(max_digits=12, decimal_places=2)

class Comment(models.Model):
    content = models.TextField()
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    time = models.DateTimeField(auto_now_add=True)

class Bid(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bids")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids")
    price = models.DecimalField(max_digits=12,decimal_places=2)