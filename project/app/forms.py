from django import forms
from .models import *

class ItemInfoForm(forms.ModelForm):
    class Meta:
        model=ItemInfo
        fields="__all__"