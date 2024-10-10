from django.contrib import admin
from django.conf import settings  # Import settings to check for DEBUG mode
from django.conf.urls.static import static  # Correct import for static files
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    # Serve media files during development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
