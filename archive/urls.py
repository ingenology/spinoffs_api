from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('archive.views',
    url(r'^$', 'archive_root', name='archive_api_root'),
)

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])
