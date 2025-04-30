from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ItemForm
from .models import Item

def index(request):
    item_list = Item.objects.all()

    # a template always needs a context, so we create one
    context = {
        'item_list': item_list,
    }
    return render(request, 'foodie/index.html', context)


def item(request):
    return HttpResponse('<h1>This is an item</h1>')
    

def details(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item': item,
    }
    return render(request, 'foodie/details.html', context)


@login_required(login_url='/login/')
def create_item(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('foodie:index')
    
    return render(request, 'foodie/item-form.html', {'form': form})


@login_required(login_url='/login/')
def update_item(request, item_id):
    item = Item.objects.get(id=item_id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('foodie:index')
    
    return render(request, 'foodie/item-form.html', {'form': form, 'item': item})


@login_required(login_url='/login/')
def delete_item(request, item_id):
    item = Item.objects.get(id=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('foodie:index')
    
    return render(request, 'foodie/item-delete.html', {'item': item})