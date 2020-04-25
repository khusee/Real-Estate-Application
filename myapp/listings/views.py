from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Listing
from django.shortcuts import get_object_or_404
from .choices import address_choices,subcategory_choices,category_choices,price_choices,district_choices,propertytype_choices,city_choices


# Create your views here.

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published = True)
    paginator = Paginator(listings,3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }
    return render(request,'listings/listings.html',context)

def listing(request, listing_id):
    listings = get_object_or_404(Listing,id = listing_id)
    context = {
        'listings': listings
    }
    return render(request,'listings/listing.html',context)

def search(request):
    query_set = Listing.objects.order_by('-list_date')
    if 'address' in request.GET:
        address = request.GET['address']
        if address:
            query_set = query_set.filter(address__icontains = address)

    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            query_set = query_set.filter(category__iexact = category)

    if 'property_type' in request.GET:
        property_type = request.GET['property_type']
        if property_type:
            query_set = query_set.filter(propertytype__iexact = property_type)

    if 'property' in request.GET:
        property = request.GET['property']
        if property:
            query_set = query_set.filter(subcategory__iexact = property)

    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            query_set = query_set.filter(price__lte = price)

    if 'prices' in request.GET:
        prices = request.GET['prices']
        if prices:
            query_set = query_set.filter(price__gte = prices)
    context = {
        'listings':query_set,
        'address_choices': address_choices,
        'category_choices': category_choices,
        'city_choices': city_choices,
        'propertytype_choices': propertytype_choices,
        'price_choices': price_choices,
        'subcategory_choices': subcategory_choices,
        'district_choices': district_choices,
        'values': request.GET
    }
    return render(request,'listings/search.html',context)
