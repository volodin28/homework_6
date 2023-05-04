from django.db import models
from student.models import Student
from teacher.models import Teacher


class Group(models.Model):
    group_name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.group_name
