from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from auctions.forms import BidForm, ListingForm

from .models import User, Listing, Bid, Comment


def index(request):
    listings = Listing.objects.all()
    return render(request, "auctions/index.html", {
        'listings': listings
    })


def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


@login_required(login_url='/login')
def create(request):
    if request.method == "POST":
        listing = Listing(user=request.user)
        listing_form = ListingForm(request.POST, instance=listing)
        if listing_form.is_valid():
            listing = listing_form.save()
        return HttpResponseRedirect(reverse("index"))
    else:
        listing_form = ListingForm()
        return render(request, 'auctions/create.html', {
            'form': listing_form,
        })


def listing(request, id):
    listing = Listing.objects.get(pk=id)
    bid_form = BidForm()
    bids = listing.bids.all()
    return render(request, 'auctions/listing.html', {
        "listing": listing,
        "bid_form" : bid_form,
        "bids" : bids
    })

@login_required(login_url='/login')    
def bid(request, id):
    listing = Listing.objects.get(pk=id)
    if request.method == "POST":
        amount = request.POST["price"]
        listing = Listing.objects.get(id=id)
        user = request.user
        bid = Bid(listing=listing, user=user)
        bids = listing.bids.all()
        if bids:
            highest_bid = listing.bids.all()[0].price
            if int(amount) <= highest_bid:
                raise ValidationError('Bid must be greater than the other bids!')
        if int(amount) < listing.starting_price:
            raise ValidationError('Bid must be greater than the starting price!')
        
        bid_form = BidForm(request.POST, instance=bid)
        if bid_form.is_valid():
            bid = bid_form.save()
            
    return HttpResponseRedirect(reverse('listing', kwargs={'id': id}))
