from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(max_length=300, unique=True)  # Ensure slug is unique

    class Meta:
        ordering = ['name']
        indexes = [models.Index(fields=['name'])]
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Event(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='events')
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300, unique=True)
    location = models.CharField(max_length=300)
    description = models.TextField()
    price = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    rating = models.DecimalField(default=0.2, max_digits=3, decimal_places=1)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    default_image = models.ImageField(upload_to="events", default="events/default_img.png", blank=True, null=True)

    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)


    def save(self, *args, **kwargs):
        if  not self.slug:
            self.slug = f"{slugify(self.name)}-slug"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class EventImage(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_image')
    image = models.ImageField(upload_to="events/images/", blank=True, null=True)

    def __str__(self):
        return self.event.default_image.url if self.event.default_image else 'No Image'
