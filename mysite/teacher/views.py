from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse

from .forms import TeacherForm
from .models import Teacher


def add_teacher(request):
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("teachers-list"))
    else:
        form = TeacherForm()
    return render(request, "add_teacher.html", {"form": form})


def teachers_list_view(request):
    teachers = Teacher.objects.all()
    return render(request, "teachers.html", {"teachers": teachers})


def edit_teacher(request, id: int):
    try:
        teacher = Teacher.objects.get(id=id)
    except Teacher.DoesNotExist:
        return HttpResponse(f"No teacher with id {id}")
    if request.method == "GET":
        form = TeacherForm(instance=teacher)
        context = {"form": form}
        return render(request, "edit_teacher.html", context)
    elif request.method == "POST":
        form = TeacherForm(request.POST, instance=teacher)
        if not form.is_valid():
            return HttpResponse("Form is not valid")
        form.save()
        return HttpResponseRedirect(reverse('teachers-list'))


def delete_teacher(request, id: int):
    if request.method == "POST":
        teacher = Teacher.objects.get(id=id)
        teacher.delete()
        return HttpResponseRedirect(reverse('teachers-list'))
