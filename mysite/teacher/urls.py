from django.urls import path

from . import views

urlpatterns = [
    path("add/", views.add_teacher, name="add-teacher"),
    path("list/", views.teachers_list_view, name="teachers-list"),
    path("edit/<int:id>", views.edit_teacher, name="edit-teacher"),
    path("delete/<int:id>", views.delete_teacher, name='delete-teacher')
]
