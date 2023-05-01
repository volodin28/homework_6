from django.urls import path

from . import views

urlpatterns = [
    path("", views.get_group, name="add-group"),
    path("groups/", views.groups_list_view, name="groups-list"),
]
