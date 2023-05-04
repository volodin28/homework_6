from django.urls import path

from . import views

urlpatterns = [
    path("students/", views.student_list_view, name="student-list"),
    path("edit/<int:id>", views.edit_student, name="edit-student"),
    path("delete/<int:id>", views.delete_student, name='delete-student')
]
