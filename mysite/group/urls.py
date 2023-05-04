from django.urls import path

from . import views

urlpatterns = [
    path("add/", views.save_group, name="add-group"),
    path("groups/", views.groups_list_view, name="groups-list"),
]
