from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ItemForm
from .models import Item
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# function view not being used anymore, is commented out in the urls.py file
# but is kept here for reference
def index(request):
    item_list = Item.objects.all()

    # a template always needs a context, so we create one
    context = {
        'item_list': item_list,
    }
    return render(request, 'foodie/index.html', context)


class IndexClassView(ListView):
    model = Item
    template_name = 'foodie/index.html'
    context_object_name = 'item_list'

def item(request):
    return HttpResponse('<h1>This is an item</h1>')
    

def details(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item': item,
    }
    return render(request, 'foodie/details.html', context)

class DetailsClassView(DetailView):
    model = Item
    template_name = 'foodie/details.html'


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
        messages.success(request, f'Item "{item.item_name}" has been deleted successfully.')
        return redirect('foodie:index')
    
    return redirect('foodie:details', pk=item_id)