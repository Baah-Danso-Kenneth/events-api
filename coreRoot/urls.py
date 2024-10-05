from django.conf import settings
from django.contrib import admin
from django.template.context_processors import static
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

