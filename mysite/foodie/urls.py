from django.urls import path

from . import views

app_name = "foodie"
urlpatterns = [
    # path("", views.index, name="index"), # this uses the function view
    path("", views.IndexClassView.as_view(), name="index"), # this uses the class view
    #path("<int:item_id>/", views.details, name="details"), # this uses the function view
    path("<int:pk>/", views.DetailsClassView.as_view(), name="details"),
    path("item", views.item, name="item"),
    path("add", views.create_item, name="create_item"),
    path("edit/<int:item_id>/", views.update_item, name="update_item"),
    path("delete/<int:item_id>/", views.delete_item, name="delete_item"),
]
