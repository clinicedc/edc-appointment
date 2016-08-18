from django.apps import AppConfig as DjangoAppConfig

from edc_appointment.apps import AppConfig as EdcAppointmentAppConfigParent


class AppConfig(DjangoAppConfig):
    name = 'example'
    verbose_name = 'Example Project'
    institution = 'Botswana-Harvard AIDS Institute Partnership'


class EdcAppointmentAppConfig(EdcAppointmentAppConfigParent):
    model = ('example', 'appointment')
