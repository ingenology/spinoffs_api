from django import forms
from django.contrib.auth.forms import AuthenticationForm


class UserAuthForm(AuthenticationForm):
    def clean(self):
        self.cleaned_data = super(UserAuthForm, self).clean()
        # custom validation here, user is in self.user_cache btw
        return self.cleaned_data
