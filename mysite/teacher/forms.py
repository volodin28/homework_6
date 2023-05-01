from django.core.exceptions import ValidationError
from django.forms import ModelForm

from .models import Teacher


class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ["first_name", "last_name"]

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if len(first_name) > 100:
            raise ValidationError('Input is too long')
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if len(last_name) > 100:
            raise ValidationError('Input is too long')
        return last_name
