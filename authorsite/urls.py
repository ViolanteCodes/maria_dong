from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from layout.views import ButterPageView, ContactFormView, CampaignFormView
from books.views import BookView

newsletter_url = settings.NEWSLETTER_LANDING_PAGE

urlpatterns = [
    path('', ButterPageView.as_view(template_name="landing_page.html"),
        {'page_slug': 'landing-page'}, name="home"),
    path('link-tree/', ButterPageView.as_view(template_name="links_page.html"),
        {'page_type':'links_page', 'page_slug': 'link-tree'}, name="link_tree"),
    path('about/', ContactFormView.as_view(template_name="about.html"),
        {'page_slug': 'about'}, name="about"),
    path('about/success/', ButterPageView.as_view(template_name="success.html"),
        {'page_slug': 'success'}, name="success"),
    path('campaigns/<page_slug>/', CampaignFormView.as_view(template_name="campaign.html"),
        {'page_type': 'campaign_page'}, name="campaign"),
    path('books/', ButterPageView.as_view(template_name="books_list.html"), 
        {'page_slug': 'books'}, name="books_list"), 
    path('books/<slug:slug>/', BookView.as_view(), name="book_page"),
    path('events/', ButterPageView.as_view(template_name="events_and_press.html"),
        {'page_slug':'events-and-press'}, name="events"),
    path('publications/', ButterPageView.as_view(template_name='shorts.html'), 
        {
            'page_slug':'publications', 
            'page_type_list':'short', 
            'params': {
                'page_size':'30',
                'order':'-publication_date',
                }
            }, name="publications"),
    # path('newsletter/', RedirectView.as_view(url=newsletter_url), name="newsletter"),
    path('newsletter/', ButterPageView.as_view(template_name="newsletter.html"),
        {'page_slug':'newsletter'},
        name="newsletter"),
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
]
