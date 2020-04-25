from django.shortcuts import render
from realtors.models import Realtor
from listings.models import Listing
from listings.choices import address_choices, category_choices,city_choices,propertytype_choices,price_choices,subcategory_choices,district_choices


from django.http import HttpResponse

# Create your views here.

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published = True)[:3]
    context = {
        'listings': listings,
        'address_choices':address_choices,
        'category_choices':category_choices,
        'city_choices': city_choices,
        'propertytype_choices': propertytype_choices,
        'price_choices': price_choices,
        'subcategory_choices':subcategory_choices,
        'district_choices': district_choices
    }
    return render(request,'pages/index.html',context)

def about(request):
    # get all realtors
    realtors = Realtor.objects.order_by('hire_date')
    # get mvp
    mvp_realtors = Realtor.objects.all().filter(is_mvp = True)
    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }
    return render(request, 'pages/about.html', context)
