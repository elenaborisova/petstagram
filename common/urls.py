from django.urls import path
from common.views import landing_page
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', landing_page, name='index'),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
