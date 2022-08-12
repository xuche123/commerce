from .models import Bid, Comment, Listing
from django.forms import ModelForm, TextInput, Textarea, NumberInput, ClearableFileInput


class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'desc', 'image', 'category', 'starting_price']
        widgets = {
            'title': TextInput(attrs={
                'class': "form-control",
            }),
            'desc': Textarea(attrs={
                'class': "form-control",
            }),
            'image': ClearableFileInput(attrs={
                'class': "form-control",
            }),
            'category': TextInput(attrs={
                'class': "form-control",
            }),
            'starting_price': NumberInput(attrs={
                'class': "form-control",
            }),
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


class BidForm(ModelForm):
    class Meta:
        model = Bid
        fields = ['price']
