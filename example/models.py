from django.utils import timezone

from django.db import models

from django_crypto_fields.crypt_model_mixin import CryptModelMixin

from edc_base.model.models import BaseUuidModel

from edc_appointment.model_mixins import AppointmentModelMixin
from edc_appointment.requires_appointment_mixin import RequiresAppointmentMixin
from edc_appointment.appointment_mixin import AppointmentMixin
from edc_meta_data.crf_meta_data_managers import CrfMetaDataManager

from simple_history.models import HistoricalRecords

from edc_meta_data.model_mixins import CrfMetaDataModelMixin, RequisitionMetaDataModelMixin
from edc_meta_data.crf_meta_data_mixin import CrfMetaDataMixin

from edc_visit_tracking.models.visit_model_mixin import VisitModelMixin
from edc_visit_tracking.models.previous_visit_mixin import PreviousVisitMixin
from edc_visit_tracking.models.crf_model_mixin import CrfModelMixin

from edc_registration.models import RegisteredSubjectModelMixin


class Crypt(CryptModelMixin, BaseUuidModel):

    class Meta:
        app_label = 'example'
        unique_together = (('hash', 'algorithm', 'mode'),)


class RegisteredSubject(RegisteredSubjectModelMixin, BaseUuidModel):

    class Meta:
        app_label = 'example'


class Appointment(AppointmentModelMixin, RequiresAppointmentMixin, BaseUuidModel):

    history = HistoricalRecords()

    class Meta:
        app_label = 'example'


class CrfMetaData(CrfMetaDataModelMixin, BaseUuidModel):

    registered_subject = models.ForeignKey(RegisteredSubject)

    appointment = models.ForeignKey(Appointment, related_name='+')

    class Meta:
        app_label = 'example'


class RequisitionMetaData(RequisitionMetaDataModelMixin, BaseUuidModel):

    registered_subject = models.ForeignKey(RegisteredSubject)

    appointment = models.ForeignKey(Appointment, related_name='+')

    class Meta:
        app_label = 'example'


class SubjectVisit(CrfMetaDataMixin, PreviousVisitMixin, VisitModelMixin, BaseUuidModel):

    appointment = models.OneToOneField(Appointment)

    class Meta:
        app_label = 'example'


class CrfOne(CrfModelMixin, BaseUuidModel):

    subject_visit = models.ForeignKey(SubjectVisit)

    f1 = models.CharField(max_length=10, null=True)

    entry_meta_data_manager = CrfMetaDataManager(SubjectVisit)

    class Meta:
        app_label = 'example'


class CrfTwo(CrfMetaDataMixin, BaseUuidModel):

    subject_visit = models.ForeignKey(SubjectVisit)

    f1 = models.CharField(max_length=10, null=True)

    entry_meta_data_manager = CrfMetaDataManager(SubjectVisit)

    class Meta:
        app_label = 'example'


class TestModel(CrfMetaDataMixin, AppointmentMixin, BaseUuidModel):
    """Triggers creation of appointments."""

    f1 = models.CharField(max_length=10, null=True)

    def get_registration_datetime(self):
        return timezone.now()

    def save(self, *args, **kwargs):
        self.prepare_appointments('default')
        super(TestModel, self).save(*args, **kwargs)

    class Meta:
        app_label = 'example'


class RequisitionOne(CrfModelMixin, BaseUuidModel):

    subject_visit = models.ForeignKey(SubjectVisit)

    class Meta:
        app_label = 'example'
