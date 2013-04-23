from .models import Fact

from rest_framework import serializers
from rest_framework.fields import Field

from archive.serializers import SimpleItemSerializer


class FactSerializer(serializers.ModelSerializer):
    spinoff = SimpleItemSerializer()
    image = Field(source='get_image_url')
    answer_image = Field(source='get_answer_image_url')
    choices = Field(source='get_choices')

    class Meta:
        model = Fact
        fields = (
            'id',
            'fact',
            #'image',
            'level',
            'question',
            'answer_text',
            'answer_image',
            'spinoff',
            'choices',
            )
