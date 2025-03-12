from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('Hello World!')


def item(request):
    return HttpResponse('<h1>This is an item</h1>')
    