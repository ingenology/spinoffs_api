from rest_framework import generics

from .models import Fact
from .serializers import FactSerializer


class FactList(generics.ListAPIView):
    model = Fact
    serializer_class = FactSerializer
    filter_fields = (
        'level',
        )

    def get_queryset(self):
        return Fact.objects.active()

fact_root = FactList.as_view()
