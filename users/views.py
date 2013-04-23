from django.contrib.auth.views import login, logout
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect

from .forms import UserAuthForm


def users_login(request, **kwargs):
    template = kwargs.get('template', 'users/login.html')
    if request.user.is_authenticated():
        return redirect(reverse_lazy('home'))
    else:
        return login(request, template_name=template, authentication_form=UserAuthForm)


def users_logout(request, **kwargs):
    logout(request)
    return redirect(reverse_lazy('login'))
