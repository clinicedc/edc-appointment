from django.apps import AppConfig as DjangoAppConfig
from django_crypto_fields.apps import AppConfig as DjangoCryptoFieldsAppConfigParent

from edc_appointment.apps import AppConfig as EdcAppointmentAppConfigParent
from edc_meta_data.apps import AppConfig as EdcMetaDataAppConfigParent


class AppConfig(DjangoAppConfig):
    name = 'example'
    verbose_name = 'Example Project'
    institution = 'Botswana-Harvard AIDS Institute Partnership'


class EdcAppointmentAppConfig(EdcAppointmentAppConfigParent):
    model = ('example', 'appointment')


class EdcMetaDataAppConfig(EdcMetaDataAppConfigParent):
    model_attrs = [('example', 'crfmetadata'), ('example', 'requisitionmetadata')]


class DjangoCryptoFieldsAppConfig(DjangoCryptoFieldsAppConfigParent):
    model = ('example', 'crypt')
    crypt_model_using = 'default'
