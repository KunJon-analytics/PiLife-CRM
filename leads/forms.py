from django import forms
from .models import Lead


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
            "provider"           
        )

class LeadForm(forms.Form):
    first_name          = forms.CharField()
    last_name           = forms.CharField()
    phone_number        = forms.IntegerField()
    email_address       = forms.EmailField()
    date_of_birth       = forms.DateField()
   