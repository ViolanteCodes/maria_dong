from django.db import models

# Create your models here.
class Image(models.Model):
    name = models.CharField()
    alt_text = models.TextField(blank=True)
    file = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.name
