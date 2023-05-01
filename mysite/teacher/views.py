from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import TeacherForm
from .models import Teacher


def get_teacher(request):
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/teacher/teachers')
    else:
        form = TeacherForm()
    return render(request, "index.html", {"form": form})


def teachers_list_view(request):
    teachers = Teacher.objects.all()
    return render(request, "teachers.html", {"teachers": teachers})
