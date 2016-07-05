from django.conf.urls import include, url
from django.contrib import admin
from example.views import HomeView

urlpatterns = [
    url(r'^edc-appointment/', include('edc_appointment.urls')),
    url(r'^edc-visit-schedule/', include('edc_visit_schedule.urls')),
    url(r'^edc-content-type-map/', include('edc_content_type_map.urls')),
    url(r'^edc-meta-data/', include('edc_meta_data.urls')),
    url(r'^django-crypto-fields/', include('django_crypto_fields.urls')),
    url(r'^edc/', include('edc_base.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', HomeView.as_view(), name='home_url'),
]
