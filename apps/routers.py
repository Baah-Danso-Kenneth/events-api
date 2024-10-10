from rest_framework import  routers

from apps.events.viewsets import EventsListAPIView


router = routers.SimpleRouter()



urlpatterns = [
    *router.urls,
]