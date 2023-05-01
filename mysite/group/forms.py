from django.core.exceptions import ValidationError
from django.forms import ModelForm

from .models import Group


class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ["group_name"]

    def clean_group_name(self):
        group_name = self.cleaned_data['group_name']
        if len(group_name) > 100:
            raise ValidationError('Input is too long')
        return group_name
