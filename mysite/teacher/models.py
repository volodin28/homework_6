from datetime import date

from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthday = models.DateField(default=date.today)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
