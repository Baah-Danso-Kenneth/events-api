from django.conf import settings
<<<<<<< HEAD
=======
from django.conf.urls.static import static
>>>>>>> e027666 (Prep project with new apps)
from django.contrib import admin
from django.template.context_processors import static
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

<<<<<<< HEAD
=======
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> e027666 (Prep project with new apps)
