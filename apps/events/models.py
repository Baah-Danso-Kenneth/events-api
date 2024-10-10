from django.db import models
from django.forms import SlugField
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(max_length=300, unique=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]
        verbose_name='category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Event(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='events')
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300)
    location = models.CharField(max_length=300)
    description = models.TextField()
    price = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)
    rating = models.DecimalField(default=0.2, max_digits=3, decimal_places=1)
    start_date = models.DateTimeField(auto_now=True)
    end_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    default_image = models.ImageField(upload_to="events/default_img.png", blank=True, null=True)

    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class EventImage(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_image')
    image = models.ImageField(upload_to="events/default_img.png", blank=True, null=True)

    def __str__(self):
        return self.event.default_img