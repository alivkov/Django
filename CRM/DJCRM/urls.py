from CRM.DJCRM.settings import STATIC_URL
from django.conf import settings
from django.conf.urls.static import static
from leads.views import LandingPageView
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('leads/', include('leads.urls', namespace="leads")),
    path('', LandingPageView.as_view(), name="landing-page")
    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
]
