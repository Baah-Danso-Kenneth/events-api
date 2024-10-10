from django.apps import AppConfig


<<<<<<<< HEAD:core/profiles/apps.py
class ProfilesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core.profiles'
========
class EventsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.events'
>>>>>>>> e027666 (Prep project with new apps):apps/events/apps.py
