from rest_framework import generics
from rest_framework.permissions import AllowAny
from apps.events.models import EventImage, Category, Event
from apps.events.serializers import EventImageSerializers, CategorySerializers, EventSerializer


class EventsListAPIView(generics.ListAPIView):
    queryset = EventImage.objects.all()  # Retrieve all EventImage instances
    serializer_class = EventImageSerializers
    permission_classes = (AllowAny,)

class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()  # Retrieve all Category instances
    serializer_class = CategorySerializers


class ALLEventListAPIView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer