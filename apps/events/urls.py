from django.urls import path

from apps.events.views import EventsListAPIView, CategoryListAPIView

urlpatterns = [
    path('all/events', EventsListAPIView.as_view(), name="event_list"),
    path('category', CategoryListAPIView.as_view(), name="category_list")
]