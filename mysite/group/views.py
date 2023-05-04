from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import GroupForm
from .models import Group


def save_group(request):
    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("groups-list"))
    else:
        form = GroupForm()
    return render(request, "index_group.html", {"form": form})


def groups_list_view(request):
    groups = Group.objects.all()
    return render(request, "groups.html", {"groups": groups})
