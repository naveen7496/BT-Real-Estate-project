from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Listing


def index(request):
    listings = Listing.objects.all()
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    print("################")
    print(paged_listings.number)
    print(paged_listings.object_list)
    print("################")
    context = {
        'listings' : paged_listings
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listing' : listing
    }
    return render(request, 'listings/listing.html', context)


def search(request):
    queryset_list = Listing.objects.order_by('-list_date')
    #Keywords
    if 'keywords' in request.GET:
        keywords = request.GET.get('keywords')
        if keywords:
            print('THE KEYWORD IS: '+keywords)
            queryset_list = queryset_list.filter(description__icontains=keywords)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)
    context = {
        'listings': queryset_list
    }
    return render(request, 'listings/search.html', context)
