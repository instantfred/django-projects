from django.http import HttpResponse
from django.shortcuts import render
from .models import Item
from django.template import loader

def index(request):
    item_list = Item.objects.all()

    # a template always needs a context, so we create one
    context = {
        'item_list': item_list,
    }
    return render(request, 'foodie/index.html', context)


def item(request):
    return HttpResponse('<h1>This is an item</h1>')
    