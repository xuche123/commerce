from django.contrib.auth.models import AbstractUser
from django.db import models

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
    
class User(AbstractUser):
    watchlist = models.ManyToManyField('Listing', related_name='watchlist', blank='true')
    pass

class Listing(models.Model):
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
    active = models.BooleanField(default=True)
    winner = models.CharField(max_length=100, blank=True, null=True)

class Comment(models.Model):
    content = models.TextField()
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-time',)

class Bid(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bids")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids")
    price = models.DecimalField(max_digits=12,decimal_places=2)
    
    class Meta:
        ordering = ('-price',)