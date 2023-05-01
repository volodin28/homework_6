from datetime import date

from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from .models import Teacher


class DateInput(forms.DateInput):
    input_type = 'date'


class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ["first_name", "last_name", "birthday"]
        widgets = {
            'birthday': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}
            )
        }

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

    def clean_birthday(self):
        birthday = self.cleaned_data['birthday']
        if birthday > date.today():
            raise ValidationError("Birthday can't be in the future")
        return birthday
