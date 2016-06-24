from django.db import models

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


class RegisteredSubject(BaseUuidModel):

    subject_identifier = models.CharField(
        verbose_name="Subject Identifier",
        max_length=50,
        blank=True,
        db_index=True,
        unique=True)

    study_site = models.CharField(
        max_length=50,
        null=True,
        blank=True)

    class Meta:
        app_label = 'example'


class AppointmentTestModel(AppointmentModelMixin, BaseUuidModel):

    registered_subject = models.ForeignKey(RegisteredSubject)

    history = AuditTrail()

    class Meta:
        app_label = 'example'


class TestModel(AppointmentMixin, BaseUuidModel):
    """Trigers creation of appointments."""

    APPOINTMENT_MODEL = AppointmentTestModel

    def save(self, *args, **kwargs):
        self.prepare_appointments()
        super(TestModel, self).save(*args, **kwargs)

    class Meta:
        app_label = 'example'
