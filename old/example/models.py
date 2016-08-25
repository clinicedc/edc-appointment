from django.utils import timezone

from django.db import models
from django_crypto_fields.crypt_model_mixin import CryptModelMixin

from edc_appointment.model_mixins import (
    AppointmentModelMixin, RequiresAppointmentModelMixin, CreateAppointmentsMixin)
from edc_base.model.models import BaseUuidModel
from edc_meta_data.managers import CrfMetaDataManager
from edc_meta_data.model_mixins import CrfMetaDataModelMixin, RequisitionMetaDataModelMixin
from edc_meta_data.mixins import CrfMetaDataMixin
from edc_visit_tracking.model_mixins import VisitModelMixin, PreviousVisitModelMixin, CrfModelMixin
from edc_registration.model_mixins import RegisteredSubjectModelMixin


class Crypt(CryptModelMixin, BaseUuidModel):

    class Meta:
        app_label = 'edc_example'
        unique_together = (('hash', 'algorithm', 'mode'),)


class RegisteredSubject(RegisteredSubjectModelMixin, BaseUuidModel):

    class Meta:
        app_label = 'edc_example'


class Appointment(AppointmentModelMixin, RequiresAppointmentModelMixin, BaseUuidModel):

    class Meta:
        app_label = 'edc_example'


class CrfMetaData(CrfMetaDataModelMixin, BaseUuidModel):

    registered_subject = models.ForeignKey(RegisteredSubject)

    appointment = models.ForeignKey(Appointment, related_name='+')

    class Meta:
        app_label = 'edc_example'


class RequisitionMetaData(RequisitionMetaDataModelMixin, BaseUuidModel):

    registered_subject = models.ForeignKey(RegisteredSubject)

    appointment = models.ForeignKey(Appointment, related_name='+')

    class Meta:
        app_label = 'edc_example'


class SubjectVisit(CrfMetaDataMixin, PreviousVisitModelMixin, VisitModelMixin, BaseUuidModel):

    appointment = models.OneToOneField(Appointment)

    class Meta:
        app_label = 'edc_example'


class CrfOne(CrfModelMixin, BaseUuidModel):

    subject_visit = models.ForeignKey(SubjectVisit)

    f1 = models.CharField(max_length=10, null=True)

    entry_meta_data_manager = CrfMetaDataManager(SubjectVisit)

    class Meta:
        app_label = 'edc_example'


class CrfTwo(CrfMetaDataMixin, BaseUuidModel):

    subject_visit = models.ForeignKey(SubjectVisit)

    f1 = models.CharField(max_length=10, null=True)

    entry_meta_data_manager = CrfMetaDataManager(SubjectVisit)

    class Meta:
        app_label = 'edc_example'


class TestModel(CrfMetaDataMixin, CreateAppointmentsMixin, BaseUuidModel):
    """Triggers creation of appointments."""

    f1 = models.CharField(max_length=10, null=True)

    def get_registration_datetime(self):
        return timezone.now()

    def save(self, *args, **kwargs):
        self.prepare_appointments('default')
        super(TestModel, self).save(*args, **kwargs)

    class Meta:
        app_label = 'edc_example'


class RequisitionOne(CrfModelMixin, BaseUuidModel):

    subject_visit = models.ForeignKey(SubjectVisit)

    class Meta:
        app_label = 'edc_example'
