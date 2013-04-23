from django import forms

from .models import Fact


class FactForm(forms.ModelForm):
    model = Fact
    fieldsets = (
        (None, {
            'fields': ('spinoff', 'fact', 'image', 'level', )
        }),
        ('Quiz', {
            'fields': ('question', 'answer_text', 'answer_image', )
        }),
    )
