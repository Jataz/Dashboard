from django import forms
from .models import Vehicle

class VehiclesForm(forms.ModelForm):
    class Meta:
        model= Vehicle
        fields= ["owner", "license_number", "mobile_number", "model","role","status"]
