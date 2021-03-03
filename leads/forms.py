from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import Lead, Provider

User = get_user_model()


class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            "first_name",
            "last_name",
            "phone_number",
            "email_address",
            "date_of_birth",
            "number_of_people",
            "health_plan",
            "provider",
            "description"
        )


class LeadForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.IntegerField()
    email_address = forms.EmailField()
    date_of_birth = forms.DateField()


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}


class AssignProviderForm(forms.Form):
    provider = forms.ModelChoiceField(queryset=Provider.objects.none())

    def __init__(self, *args, **kwargs):
        request = kwargs.pop("request")
        providers = Provider.objects.filter(
            organisation=request.user.userprofile)
        super(AssignProviderForm, self).__init__(*args, **kwargs)
        self.fields["provider"].queryset = providers


class LeadCategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ('category',)
