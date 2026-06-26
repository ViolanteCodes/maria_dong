from django.views.generic import TemplateView
from seo.mixins import SEOBlockMixin
from press.models import PressArticle
from press.models import RecordedEvent
from press.models import Event

# Create your views here.

class PressView(SEOBlockMixin, TemplateView):
    seo_block_slug = "press"
    template_name = "events_and_press.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["events"] = Event.objects.all()
        context["recorded"] = RecordedEvent.objects.all()
        context["articles"] = PressArticle.objects.all()
        return context

class NewsletterView(SEOBlockMixin, TemplateView):
    seo_block_slug = "newsletter"
    template_name = "newsletter.html"
