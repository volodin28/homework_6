from django.db import models

from teacher.models import Teacher


class Group(models.Model):
    group_name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
