from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from books.views import BookView
from books.views import BooksListView
from shorts.views import ShortsListView
from press.views import PressView
from about.views import AboutView
from about.views import SuccessView
from press.views import NewsletterView
from linktree.views import LinkTreeView
from layout.views import LandingView

newsletter_url = settings.NEWSLETTER_LANDING_PAGE

urlpatterns = [
    path('', LandingView.as_view(), name="home"),
    path('link-tree/', LinkTreeView.as_view(),name="link_tree"),
    path('about/', AboutView.as_view(), name="about"),
    path('about/success/', SuccessView.as_view(), name="success"),
    # path('campaigns/<page_slug>/', CampaignFormView.as_view(template_name="campaign.html"),
    #     {'page_type': 'campaign_page'}, name="campaign"),
    path('books/', BooksListView.as_view(), name="books_list"), 
    path('books/<slug:slug>/', BookView.as_view(), name="book_page"),
    path('events/', PressView.as_view(), name="events"),
    path('publications/', ShortsListView.as_view(), name="publications"),
    path('newsletter/', NewsletterView.as_view(), name="newsletter"),
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root = settings.MEDIA_ROOT
    )
