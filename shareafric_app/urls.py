from django.urls import path
from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
app_name = 'wisteen'

urlpatterns = [
    # Add your URL patterns here
    path('', views.main, name='main'),
    path('contactUs', views.contactUs, name='contactUs'),
    # other paths...
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    path('sitemap.xml', TemplateView.as_view(template_name="sitemap.xml", content_type="application/xml")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
