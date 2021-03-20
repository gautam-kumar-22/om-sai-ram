# urls.py
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name="home"),
    path('about', AboutUSView.as_view(), name="about"),
    path('why', WhyView.as_view(), name="why"),
    path('services', ServiceView.as_view(), name="services"),
    path('contact', ContactView.as_view(), name="contact"),
    path('enquiry', EnquiryView.as_view(), name="enquiry"),
    path('service_details/<int:key_id>/', DetailsView.as_view(), name="service-details"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)