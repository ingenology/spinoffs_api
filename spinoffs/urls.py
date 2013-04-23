from django.conf import settings
from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView

from djunk_drawer.views import RobotsTxtView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', RedirectView.as_view(url='/v1/')),
    #url(r'^login/$', 'users.views.users_login', name='login'),
    #url(r'^logout/$', 'users.views.users_logout', name='logout'),
    # url(r'^foo/', include('apps.foo.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^v1/$', 'spinoffs.views.api_root', name='api_root'),
    url(r'^v1/facts/', include('facts.urls')),
    url(r'^v1/archive/', include('archive.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # robots.txt, see djunk_drawer.views.RobotsTxtView
    url('^robots.txt', RobotsTxtView.as_view())
)

urlpatterns += patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
