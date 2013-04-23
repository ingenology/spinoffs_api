from django import forms

from .models import Item

class ItemForm(forms.ModelForm):
    model = Item
