from django.shortcuts import render, get_object_or_404, HttpResponse
from home.models import AboutPage, AboutPromotion, Event, ShopCategory, Business, CategoryImage
from django.http import JsonResponse
import json
from django.core import serializers
from django.utils import timezone
import datetime
from django.template import defaultfilters


def merchants_serializer(merchants):
    actual_data = []
    
    raw_data = serializers.serialize('python', merchants)
    
    for merchant in raw_data:
        d = {}
        for field, value in merchant['fields'].items():
            if field == 'description':
                d[field] = defaultfilters.linebreaks(value)
            else:
                d[field] = value
        m = merchant['fields']
        
        maps = "https://www.google.com/maps/embed/v1/place?key=AIzaSyC-qMrBgINIQiRrEcdlz8rT6PJWEB-NvGs&q={}+{}+{}+{}".format(
            m['street'], 
            m['city'], 
            m['state'], 
            m['zip']
        )
        
        d['googMapsUrl'] = '+'.join(maps.split())
        d['id'] = merchant['pk']
        actual_data.append(d)
    
    return actual_data
    
def event_serializer(events):
    actual_data = []
    
    raw_data = serializers.serialize('python', events)
    
    for event in raw_data:
        e = event['fields']
        # Manually create the dictionary for Event querysets
        startdate = datetime.datetime.combine(e['date'], e['starttime'])
        enddate = datetime.datetime.combine(e['date'], e['endtime'])
        actual_data.append(
            dict(
                description=e['description'],
                title=e['title'],
                id=event['pk'],
                startdate=startdate,
                enddate=enddate,
                concat=e['title'].split()[0] + str(e['date']).replace('-', ''),
                eventimage=e['eventimage']
            )    
        )
        
    return actual_data

def complex_serializer(data):
    """A custom serializer that returns python without the 'fields' dicts."""
    raw_data = serializers.serialize('python', data)

    # now extract the inner `fields` dicts
    actual_data = [d['fields'] for d in raw_data]

    return actual_data


# Create your views here.
def index(request):
    
    return render(request, 'home/index.html')

def category(request, catname):
    categorymodel = get_object_or_404(ShopCategory, name__iexact=catname)

    shops = Business.objects.filter(category_id=categorymodel.id)
    catimages = CategoryImage.objects.filter(category_id=categorymodel.id)

    try:
        carousel_imgs = []
        active = True
        for i, _ in enumerate(range(0, 3)):
            if i >= 1:
                active = False
            item = {'active': active, 'image': catimages[i]}
            carousel_imgs.append(item)
    except IndexError:
        carousel_imgs = False
    
    return render(
        request, 'home/category.html', {
            'shops': shops, 'carousel_imgs': carousel_imgs, 
            'categoryname': categorymodel
            }
        )


def details(request, pk):
    shop = get_object_or_404(Business, pk=pk)
    categoryname = ShopCategory.objects.get(pk=shop.category.id)

    return render(request, 'home/details.html', {'shop': shop, 'categoryname': categoryname})


def about(request):
    about_page = AboutPage.objects.order_by('-pk')[0]
    harvestfestival = Event.objects.filter(title__icontains="harvest festival").filter(date__gte=timezone.now())
    streetfair = Event.objects.filter(title__icontains="street fair").filter(date__gte=timezone.now())
    try:
        hf = harvestfestival[0]
    except IndexError:
        hf = None
    
    try:        
        sf = streetfair[0]
    except IndexError:
        sf = None

    return render(request, 'home/about.html', {
        'about': about_page, 'harvestfestival': hf, 'streetfair': sf,
        'active_item': 'about'
        })

def events(request):
    upcoming_events = Event.objects.filter(date__gt=timezone.now()).order_by("date")
    todays_events = Event.objects.filter(date=timezone.now()).order_by("date")

    return render(request, 'home/events.html', {
        'upcoming_events': upcoming_events,
        'todays_events': todays_events,
        'active_item': 'events'})

        
        
# ANGULAR VIEWS:
def get_all_categories(request):
    categories_q = ShopCategory.objects.all()
    return JsonResponse(complex_serializer(categories_q), safe=False)

def get_all_events(request):
    future_events = Event.objects.filter(date__gt=timezone.now()).order_by("date")
    todays_events = Event.objects.filter(date=timezone.now()).order_by("date")
    
    payload = {}
    
    if future_events:
        payload["futureEvents"] = event_serializer(future_events)
    
    if todays_events:
        payload["todaysEvents"] = event_serializer(todays_events)
    
    return JsonResponse(payload)

def get_about_page(request):
    about_page = AboutPage.objects.order_by('-pk')[0]
    promos = AboutPromotion.objects.filter(aboutpage__id=about_page.id)
    harvestfestival = Event.objects.filter(title__icontains="harvest festival").filter(date__gte=timezone.now())
    streetfair = Event.objects.filter(title__icontains="street fair").filter(date__gte=timezone.now())
    

    payload = complex_serializer([about_page])[0]
    
    payload['promos'] = complex_serializer(promos)

    for ap in payload['promos']:
        del ap['aboutpage']
    
    try:
        hf = harvestfestival[0]
        payload['harvestfestival'] = '{}{}'.format(hf.title.split()[0], str(hf.date).replace('-', ''))
    except IndexError:
        pass
    
    try:        
        sf = streetfair[0]
        payload['streetfair'] = '{}{}'.format(sf.title.split()[0], str(sf.date).replace('-', ''))
    except IndexError:
        pass
    
    
    return JsonResponse(payload)
    
    
def get_merchants_by_category(request, catname):
    categorymodel = get_object_or_404(ShopCategory, name__iexact=catname)

    shops = Business.objects.filter(category_id=categorymodel.id)
    catimages = CategoryImage.objects.filter(category_id=categorymodel.id)
    
    carousel_imgs = complex_serializer(catimages)
    carousel_imgs[0]['active'] = True
    
    payload = {
        "carousel_imgs": carousel_imgs,
        "merchants": merchants_serializer(shops),
        "categoryname": catname,
    }
    
    return JsonResponse(payload)
    
def get_merchant_by_id(request, m_id):
    merchant = Business.objects.get(pk=m_id)
    payload = complex_serializer([merchant])[0]
    return JsonResponse(payload, safe=False)