from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from Realtors .models import Realtor

# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings' : listings
    }
    return render(request, 'pages/index.html', context)

def about(request):
    realtors = Realtor.objects.all()
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    context = {
        'realtors' : realtors,
        'mvp_realtors' : mvp_realtors
    }
    return render(request, 'pages/about.html', context)

def test(request):
    return render(request, 'pages/test.html')