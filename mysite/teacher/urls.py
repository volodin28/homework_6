from django.urls import path

from . import views

urlpatterns = [
    path("", views.get_teacher, name="add-teacher"),
    path("teachers/", views.teachers_list_view, name="teachers-list"),
]
