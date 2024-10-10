from rest_framework import  generics
from rest_framework.permissions import AllowAny
from apps.events.models import EventImage, Event, Category
from apps.events.serializers import EventImageSerializers, CategorySerializers


class EventsListAPIView(generics.ListAPIView):
    queryset = EventImage
    serializer_class = EventImageSerializers
    permission_classes = (AllowAny,)

class CategoryListAPIView(generics.ListAPIView):
    queryset = Category
    serializer_class = CategorySerializers