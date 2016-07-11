from django.apps import AppConfig
from django_crypto_fields.apps import DjangoCryptoFieldsAppConfig as DjangoCryptoFieldsAppConfigParent

from edc_appointment.apps import EdcAppointmentAppConfig as EdcAppointmentAppConfigParent
from edc_meta_data.apps import EdcMetaDataAppConfig as EdcMetaDataAppConfigParent


class ExampleAppConfig(AppConfig):
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
