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
    og_image = models.ForeignKey('images.Image', null=True, blank=True, on_delete=models.SET_NULL)
    og_title = models.CharField(blank=True, max_length=255)
    og_description = models.CharField(blank=True, max_length=500)
    og_type = models.CharField(choices=OG_TYPE_CHOICES, max_length=20)
    slug = models.CharField(blank=True)

    @property
    def alt_text(self):
        if self.og_image:
            return self.og_image.alt_text
        return ''

    def __str__(self):
        return self.name
