from django.db import models

OG_TYPE_CHOICES = [
    ("article", "article"),
    ("book", "book"),
    ("profile", "profile"),
    ("website", "website"),
]

class SEOBlock(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(blank=True, max_length=255)
    description = models.CharField(blank=True, max_length=500)
    og_title = models.CharField(blank=True, max_length=255)
    og_description = models.CharField(blank=True, max_length=500)
    og_image = models.ImageField(blank=True)
    alt_text = models.TextField(blank=True)
    og_type = models.CharField(choices=OG_TYPE_CHOICES, max_length=20)

    def __str__(self):
        return self.name
