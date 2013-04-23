from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('facts.views',
    url(r'^$', 'fact_root', name='fact_api_root'),
)

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])
