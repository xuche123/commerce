from .models import Bid, Comment, Listing
from django.forms import ModelForm

class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'desc', 'image', 'category' , 'starting_price']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class BidForm(ModelForm):
    class Meta:
        model = Bid
        fields = ['price']