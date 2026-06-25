from seo.models import SEOBlock

class SEOBlockMixin:
    """Mixin that provides access to all Butter Methods"""

    seo_block_slug = None

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        if self.seo_block_slug:
            context["seo_block"] = SEOBlock.objects.filter(slug=self.seo_block_slug).first()
        return context
