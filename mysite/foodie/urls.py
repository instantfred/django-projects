from django.urls import path

from . import views

app_name = "foodie"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:item_id>/", views.details, name="details"),
    path("item", views.item, name="item"),
    path("add", views.create_item, name="create_item"),
    path("edit/<int:item_id>/", views.update_item, name="update_item"),
]
