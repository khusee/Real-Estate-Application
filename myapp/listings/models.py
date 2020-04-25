from django.db import models
from datetime import datetime
from realtors.models import Realtor

# Create your models here.

class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING )
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    kitchen = models.IntegerField(default=0)
    living = models.IntegerField(default=0)
    floors = models.DecimalField(default=1, max_digits=2, decimal_places=1, blank=True)
    subcategory = models.CharField(default='House', max_length=100)
    propertytype = models.CharField(default='Residential', max_length=100, blank=True)
    category = models.CharField(max_length=200, default='Sale')
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    photo_main = models.ImageField(upload_to='photo/%Y/%m/%d')
    photo_1 = models.ImageField(upload_to='photo/%Y/%m/%d', blank=True)
    photo_2 = models.ImageField(upload_to='photo/%Y/%m/%d', blank=True)
    photo_3 = models.ImageField(upload_to='photo/%Y/%m/%d', blank=True)
    photo_4 = models.ImageField(upload_to='photo/%Y/%m/%d', blank=True)
    photo_5 = models.ImageField(upload_to='photo/%Y/%m/%d', blank=True)
    photo_6 = models.ImageField(upload_to='photo/%Y/%m/%d', blank=True)
    is_published = models.BooleanField()
    list_date = models.DateTimeField(default=datetime.now(), blank=True)
    def  __str__(self):
        return self.title