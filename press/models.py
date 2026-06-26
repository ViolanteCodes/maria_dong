from django.db import models
from ckeditor.fields import RichTextField

RECORDED_EVENT_CHOICES = [
    ('video', 'video'),
    ('audio', 'audio')
]

class Event(models.Model):
    date = models.DateTimeField()
    event_name = models.CharField()
    location_name = models.CharField(blank=True)
    location_address = models.CharField(blank=True)
    description = RichTextField(blank=True)
    link = models.URLField(blank=True)

    def __str__(self):
        return self.event_name

class RecordedEvent(models.Model):
    type = models.CharField(choices=RECORDED_EVENT_CHOICES)
    venue = models.CharField(blank=True)
    file = models.FileField(blank=True, null=True)
    link = models.URLField(blank=True)
    description = models.CharField(blank=True)
    date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        if self.venue:
            return f"{self.venue} - {self.description}"
        return self.description

class PressArticle(models.Model):
    title = models.CharField()
    url = models.URLField(blank=True)
    publication_date = models.DateTimeField(blank=True, null=True)
    published_in = models.CharField(blank=True)

    def __str__(self):
        return self.title
