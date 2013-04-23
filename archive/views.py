from rest_framework import generics

from .models import Item
from .serializers import ItemSerializer


class ItemList(generics.ListAPIView):
    model = Item
    serializer_class = ItemSerializer
    filter_fields = (
        'year',
        'title',
        'category',
        )

archive_root = ItemList.as_view()
