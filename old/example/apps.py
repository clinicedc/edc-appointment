from django.apps import AppConfig as DjangoAppConfig

from edc_appointment.apps import AppConfig as EdcAppointmentAppConfigParent

from edc_registration.apps import AppConfig as EdcRegistrationAppConfigParent


class AppConfig(DjangoAppConfig):
    name = 'edc_example'
    verbose_name = 'Example Project'
    institution = 'Botswana-Harvard AIDS Institute Partnership'


class EdcAppointmentAppConfig(EdcAppointmentAppConfigParent):
    model = ('edc_example', 'appointment')


class EdcRegistrationAppConfigAppConfig(EdcRegistrationAppConfigParent):
    model = ('edc_example', 'registeredsubject')
