from django import forms
from leads.models import Provider


class ProviderModelForm(forms.ModelForm):
    class Meta:
        model = Provider
        fields = (
            'user',
        )