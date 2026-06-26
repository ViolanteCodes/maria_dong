from django.contrib import admin
from press.models import Event
from press.models import RecordedEvent
from press.models import PressArticle

# Register your models here.

admin.site.register(Event)
admin.site.register(RecordedEvent)
admin.site.register(PressArticle)
