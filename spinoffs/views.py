from django.views.generic import TemplateView

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


class HomeView(TemplateView):
    template_name = 'base.html'

home_view = HomeView.as_view()


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'spinoffs': reverse('archive_api_root', request=request),
        'facts': reverse('fact_api_root', request=request),
    })
