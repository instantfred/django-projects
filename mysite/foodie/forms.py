from django import forms
from .models import Item

# we need a class for each form
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_name', 'item_description', 'item_price', 'item_image']