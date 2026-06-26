from django.db import models

# Create your models here.

class Link(models.Model):
    display_text = models.CharField()
    url = models.URLField()

    def __str__(self):
        return self.display_text
