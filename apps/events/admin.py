from django.contrib import admin
from apps.events.models import Category, Event, EventImage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':('name',)}

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'location','price', 'rating', 'start_date', 'end_date']
    list_filter = ['name', 'location','price', 'rating', 'start_date', 'end_date','active']
    prepopulated_fields = {'slug':('name',)}

@admin.register(EventImage)
class EventImageAdmin(admin.ModelAdmin):
    list_display = ['event', 'image']
    list_filter = ['event', 'image']