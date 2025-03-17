from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:item_id>/", views.details, name="details"),
    path("item", views.item, name="item")
]
