from django.contrib import admin
from .models import Item

# Register your models here.
# This code registers the Item model with the Django admin site. 
# This makes the Item model accessible via the Django admin interface.
admin.site.register(Item)