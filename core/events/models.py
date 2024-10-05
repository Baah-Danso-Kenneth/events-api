from django.db import models
from django.template.defaultfilters import title


class EventCategories(models.Model):
    title = models.CharField(max_length=300)
    def __str__(self):
        return  self.title

class Events(models.Model):
    category = models.ForeignKey(EventCategories, on_delete=models.PROTECT)
    name = models.CharField(max_length=300)
    slug = models.SlugField(unique=True, max_length=300)
    description = models.TextField()
    events_image = models.ImageField(blank=True,default='events/default.png')
    location = models.CharField(max_length=300)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return  self.name


