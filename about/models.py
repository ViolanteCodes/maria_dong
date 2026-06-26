from django.db import models
from ckeditor.fields import RichTextField

class SocialIcon(models.Model):
    service_name = models.CharField()
    link = models.URLField()
    fa_abbreviation = models.CharField()

    def __str__(self):
        return self.service_name

class AboutPage(models.Model):
    photo_name = models.CharField(blank=True)
    photo = models.FileField(blank=True, null=True)
    alt_text = models.CharField(blank=True)
    photo_attribution = models.CharField(blank=True)
    photo_url = models.URLField(blank=True)
    makeup_attribution = models.CharField(blank=True)
    makeup_url = models.URLField(blank=True)
    short_biography = RichTextField(blank=True)
    long_biography = RichTextField(blank=True)

    @property
    def social_icons(self):
        return SocialIcon.objects.all()



