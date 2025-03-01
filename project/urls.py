from django.contrib import admin
from django.urls import path
from app.views import create_campaign, campaign_detail, donate, home  # Import home view

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),  # Add the home page URL path

    path('donate/', donate, name='donate'),  # Add path for donate page
    path('create/', create_campaign, name='create_campaign'),  # Add path for creating a campaign
    path('campaign/<int:id>/', campaign_detail, name='campaign_detail'),  # Add path for campaign details

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)