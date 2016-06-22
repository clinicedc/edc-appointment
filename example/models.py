from django.db import models

from edc_base.model.models.base_uuid_model import BaseUuidModel
from edc_sync.models import SyncModelMixin
from django_crypto_fields.crypt_model_mixin import CryptModelMixin
from edc_appointment.models import AppointmentModelMixin, AppointmentMixin


class Crypt(CryptModelMixin, SyncModelMixin, BaseUuidModel):

    class Meta:
        app_label = 'example'
        unique_together = (('hash', 'algorithm', 'mode'),)


class Appointment (AppointmentModelMixin, BaseUuidModel):

    class Meta:
        verbose_name = 'Appointment'


class TestModel (AppointmentMixin, BaseUuidModel):

    objects = models.Manager()

    class Meta:
        app_label = 'example'
