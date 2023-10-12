from django import forms
from .models import *


class stateform(forms.ModelForm):
    class Meta:
        model = State
        fields = '__all__'

class cityform(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'

class ServiceCatogoryForm(forms.ModelForm):
    class Meta:
        model=ServiceCatogarys
        fields = ('Name', 'img', 'Description')