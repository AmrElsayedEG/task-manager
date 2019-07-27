from django import forms

from task.models import task


class taskForm(forms.ModelForm):
    class Meta:
        model = task
        fields = ('__all__')
