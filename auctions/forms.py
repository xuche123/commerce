from .models import Bid, Comment, Listing
from django.forms import ModelForm, TextInput, Textarea, NumberInput, URLInput, Select


class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'desc', 'image_url', 'category', 'starting_price']
        widgets = {
            'title': TextInput(attrs={
                'class': "form-control",
            }),
            'desc': Textarea(attrs={
                'class': "form-control",
            }),
            'image_url': URLInput(attrs={
                'class': "form-control",
            }),
            'category': Select(attrs={
                'class': "form-select",
            }),
            'starting_price': NumberInput(attrs={
                'class': "form-control",
            }),
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': Textarea(attrs={
                'class': "form-control",
                'rows' : 5,
                'placeholder' : 'write your comment here....'
            }),
        }


class BidForm(ModelForm):
    class Meta:
        model = Bid
        fields = ['price']
