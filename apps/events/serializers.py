from rest_framework import serializers
from apps.events.models import EventImage, Event, Category


class EventImageSerializers(serializers.ModelSerializer):
    class Meta:
        model=EventImage
        fields = ['__all__']

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model=Category
        field = 'name'