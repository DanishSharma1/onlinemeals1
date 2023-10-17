from django.http import HttpResponse, HttpResponseRedirect
from re import template
from django.shortcuts import render
from django.template import loader
from .models import Hotel
from django.urls import reverse



# Create your views here.


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def add(request):
    myhotel = Hotel.objects.all().values()
    template = loader.get_template("oct6.html")
    context = {
        'myhotel': myhotel
    }
    return HttpResponse(template.render(context, request))


def hotel(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))


def addrecord(request):
    x = request.POST['Item']
    y = request.POST['Price']
    myhotel = Hotel(ItemName=x, Price=y)
    myhotel.save()
    return HttpResponseRedirect(reverse('add'))


def delete(request, id):
    myhotel = Hotel.objects.get(id=id)
    myhotel.delete()
    return HttpResponseRedirect(reverse('add'))


def update(request, id):
    myhotel = Hotel.objects.get(id=id)
    template = loader.get_template('update1.html')
    context = {
        'myhotel': myhotel
    }
    return HttpResponse(template.render(context, request))


def updaterecord(request, id):
    item = request.POST['item']
    price = request.POST['price']
    myhotel = Hotel.objects.get(id=id)
    myhotel.ItemName = item
    myhotel.Price = price
    myhotel.save()
    return HttpResponseRedirect(reverse('add'))
