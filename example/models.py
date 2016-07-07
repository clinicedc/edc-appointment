from django.db import models

from datetime import datetime

from django_crypto_fields.crypt_model_mixin import CryptModelMixin
from edc_base.model.models import BaseUuidModel
from edc_appointment.model_mixins import AppointmentModelMixin
from edc_appointment.appointment_mixin import AppointmentMixin
from simple_history.models import HistoricalRecords
from edc_meta_data.model_mixins import CrfMetaDataModelMixin, RequisitionMetaDataModelMixin
from edc_meta_data.crf_meta_data_mixin import CrfMetaDataMixin
from edc_visit_tracking.models.visit_model_mixin import VisitModelMixin
from edc_visit_tracking.models.previous_visit_mixin import PreviousVisitMixin
from edc_visit_tracking.models.crf_model_mixin import CrfModelMixin
from edc_meta_data.crf_meta_data_managers import CrfMetaDataManager
from edc_consent.models.base_consent import BaseConsent
from edc_consent.models.fields.bw.identity_fields_mixin import IdentityFieldsMixin
from edc_consent.models.fields.sample_collection_fields_mixin import SampleCollectionFieldsMixin
from edc_consent.models.fields.vulnerability_fields_mixin import VulnerabilityFieldsMixin
from edc_consent.models.fields.personal_fields_mixin import PersonalFieldsMixin
from edc_consent.models.fields.site_fields_mixin import SiteFieldsMixin
from django.utils import timezone


class Crypt(CryptModelMixin, BaseUuidModel):

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


class SubjectConsent(
        BaseConsent, IdentityFieldsMixin, SampleCollectionFieldsMixin,
        SiteFieldsMixin, PersonalFieldsMixin, VulnerabilityFieldsMixin, BaseUuidModel):

    objects = models.Manager()

    class Meta:
        app_label = 'example'
        unique_together = (
            ('subject_identifier', 'version'),
            ('identity', 'version'),
            ('first_name', 'dob', 'initials', 'version'))


class Appointment(AppointmentModelMixin, BaseUuidModel):

    # registered_subject = models.ForeignKey(RegisteredSubject)

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
