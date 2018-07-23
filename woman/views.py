from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from .models import PhotoClothing
from .models import Clothing



#--------------------------------- list of clothing ------------------------------------------------------
def ListOfClothing(request):
    list_of_item = Clothing.objects.order_by('title')
    #list_of_item = Clothing.objects.get(title='african gucci')

    photos = PhotoClothing.objects.filter()

    template = loader.get_template('general.html')
    context = {
        'list_of_item' : list_of_item,
        'photos' : photos,
    }
    return HttpResponse(template.render(context, request))

#----------------------------------- item detail ----------------------------------------------------
def ItemDetail(request,keyword):
    #list_of_item = Clothing.objects.order_by('title') clothing_name=item.id
    item = Clothing.objects.get(title=keyword)
    photos = PhotoClothing.objects.filter(clothing_name=item.id)
    template = loader.get_template('item_detail.html')
    context = {
        'item' : item,
        'photos' : photos,
    }
    return HttpResponse(template.render(context, request))
#---------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------
