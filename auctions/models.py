from django.contrib.auth.models import AbstractUser
from django.db import models
from django.template.defaultfilters import slugify
from tempfile import NamedTemporaryFile
from django.core.files import File
from urllib.request import urlopen
import os


class User(AbstractUser):
    pass

class Listing(models.Model):
    title = models.CharField(max_length=64)
    desc = models.TextField()
    image = models.URLField(blank=True)

    category = models.CharField(max_length=64)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sales")
    time_created = models.DateTimeField(auto_now_add=True)
    # start_time = models.DateTimeField()
    # end_time = models.DateTimeField()
    starting_price = models.DecimalField(max_digits=12, decimal_places=2)

    def save(self, *args, **kwargs):
        string = "{}".format(self.title)
        slug = slugify(string)
        if self.image:
            img_temp = NamedTemporaryFile(delete=True)
            img_temp.write(urlopen(self.image).read())
            img_temp.flush()
            filename, file_extension = os.path.splitext(
                self.image)
            self.image.save(f"{slug}{file_extension}", File(img_temp))
        super(Listing, self).save(*args, **kwargs)

class Comment(models.Model):
    content = models.TextField()
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    time = models.DateTimeField(auto_now_add=True)

class Bid(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bids")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids")
    price = models.DecimalField(max_digits=12,decimal_places=2)