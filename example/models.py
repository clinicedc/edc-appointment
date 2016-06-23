from django_crypto_fields.fields import EncryptedCharField
from django_crypto_fields.crypt_model_mixin import CryptModelMixin
from edc_sync.models import SyncHistoricalRecords as AuditTrail
from edc_base.model.models import BaseUuidModel
from edc_sync.models import SyncModelMixin
from edc_appointment.models import AppointmentModelMixin, AppointmentMixin


class Crypt(CryptModelMixin, SyncModelMixin, BaseUuidModel):

    class Meta:
        app_label = 'example'
        unique_together = (('hash', 'algorithm', 'mode'),)


class Appointment(AppointmentModelMixin, BaseUuidModel):

    history = AuditTrail()

    class Meta:
        app_label = 'example'


class TestModel(AppointmentMixin, BaseUuidModel):
    """Trigers creation of appointments."""

    class Meta:
        app_label = 'example'
