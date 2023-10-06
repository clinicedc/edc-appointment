from datetime import date

from django.db import models
from django.db.models.deletion import PROTECT
from edc_consent.model_mixins import RequiresConsentFieldsModelMixin
from edc_crf.model_mixins import CrfModelMixin
from edc_identifier.managers import SubjectIdentifierManager
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierFieldMixin
from edc_list_data.model_mixins import ListModelMixin
from edc_metadata.model_mixins.creates import CreatesMetadataModelMixin
from edc_model.models import BaseUuidModel
from edc_offstudy.model_mixins import OffstudyModelMixin
from edc_reference.model_mixins import ReferenceModelMixin
from edc_registration.model_mixins import UpdatesOrCreatesRegistrationModelMixin
from edc_screening.model_mixins import ScreeningModelMixin
from edc_sites.models import SiteModelMixin
from edc_utils import get_utcnow
from edc_visit_schedule.model_mixins import (
    OffScheduleModelMixin,
    OnScheduleModelMixin,
    VisitCodeFieldsModelMixin,
)
from edc_visit_schedule.models import VisitSchedule
from edc_visit_tracking.model_mixins import (
    SubjectVisitMissedModelMixin,
    VisitModelMixin,
)
from edc_visit_tracking.models import SubjectVisitMissedReasons

from edc_appointment.model_mixins.next_appointment_crf_model_mixin import (
    NextAppointmentCrfModelMixin,
)
from edc_appointment.utils import get_appointment_model_name


class Panel(ListModelMixin):
    class Meta:
        pass


#
class SubjectVisit(
    SiteModelMixin,
    VisitModelMixin,
    ReferenceModelMixin,
    CreatesMetadataModelMixin,
    RequiresConsentFieldsModelMixin,
    BaseUuidModel,
):
    appointment = models.OneToOneField(get_appointment_model_name(), on_delete=PROTECT)

    subject_identifier = models.CharField(max_length=25, null=True)

    report_datetime = models.DateTimeField()

    reason = models.CharField(max_length=25, null=True)


# leave this model so ensure tests pass even though a proxy related
# visit exists (but is not used)
class SubjectVisit2(SubjectVisit):
    class Meta:
        proxy = True


class SubjectRequisition(
    SiteModelMixin,
    NonUniqueSubjectIdentifierFieldMixin,
    VisitCodeFieldsModelMixin,
    BaseUuidModel,
):
    @classmethod
    def related_visit_model_attr(cls):
        return "subject_visit"

    subject_visit = models.ForeignKey(SubjectVisit, on_delete=models.PROTECT, related_name="+")

    panel = models.ForeignKey(Panel, on_delete=PROTECT)

    class Meta(BaseUuidModel.Meta):
        pass


class SubjectVisitMissed(SiteModelMixin, SubjectVisitMissedModelMixin, BaseUuidModel):
    subject_visit = models.OneToOneField(SubjectVisit, on_delete=PROTECT)

    report_datetime = models.DateTimeField(default=get_utcnow)

    missed_reasons = models.ManyToManyField(
        SubjectVisitMissedReasons, blank=True, related_name="missed_reasons"
    )

    @classmethod
    def related_visit_model_attr(cls):
        return "subject_visit"

    @property
    def related_visit(self):
        return self.subject_visit

    class Meta(BaseUuidModel.Meta):
        verbose_name = "Missed Visit Report"
        verbose_name_plural = "Missed Visit Report"


class SubjectConsent(
    SiteModelMixin,
    NonUniqueSubjectIdentifierFieldMixin,
    UpdatesOrCreatesRegistrationModelMixin,
    BaseUuidModel,
):
    report_datetime = models.DateTimeField(default=get_utcnow)

    consent_datetime = models.DateTimeField(default=get_utcnow)

    version = models.CharField(max_length=25, default="1")

    identity = models.CharField(max_length=25)

    confirm_identity = models.CharField(max_length=25)

    dob = models.DateField(default=date(1995, 1, 1))


class SubjectScreening(ScreeningModelMixin, BaseUuidModel):
    objects = SubjectIdentifierManager()


class SubjectOffstudy(SiteModelMixin, OffstudyModelMixin, BaseUuidModel):
    objects = SubjectIdentifierManager()


class SubjectOffstudy2(SiteModelMixin, OffstudyModelMixin, BaseUuidModel):
    objects = SubjectIdentifierManager()


class SubjectOffstudyFive(SiteModelMixin, OffstudyModelMixin, BaseUuidModel):
    objects = SubjectIdentifierManager()


class SubjectOffstudySix(SiteModelMixin, OffstudyModelMixin, BaseUuidModel):
    objects = SubjectIdentifierManager()


class SubjectOffstudySeven(SiteModelMixin, OffstudyModelMixin, BaseUuidModel):
    objects = SubjectIdentifierManager()


class DeathReport(SiteModelMixin, BaseUuidModel):
    subject_identifier = models.CharField(max_length=25, null=True)

    report_datetime = models.DateTimeField()


# visit_schedule


class OnSchedule(SiteModelMixin, OnScheduleModelMixin, BaseUuidModel):
    pass


class OffSchedule(SiteModelMixin, OffScheduleModelMixin, BaseUuidModel):
    pass


class OnScheduleOne(SiteModelMixin, OnScheduleModelMixin, BaseUuidModel):
    pass


class OffScheduleOne(SiteModelMixin, OffScheduleModelMixin, BaseUuidModel):
    class Meta(OffScheduleModelMixin.Meta):
        pass


class OnScheduleTwo(SiteModelMixin, OnScheduleModelMixin, BaseUuidModel):
    pass


class OffScheduleTwo(SiteModelMixin, OffScheduleModelMixin, BaseUuidModel):
    pass


class OnScheduleThree(SiteModelMixin, OnScheduleModelMixin, BaseUuidModel):
    pass


class OffScheduleThree(SiteModelMixin, OffScheduleModelMixin, BaseUuidModel):
    pass


class OnScheduleSix(SiteModelMixin, OnScheduleModelMixin, BaseUuidModel):
    pass


class OffScheduleSix(SiteModelMixin, OffScheduleModelMixin, BaseUuidModel):
    pass


class CrfOne(CrfModelMixin, BaseUuidModel):
    subject_visit = models.ForeignKey(SubjectVisit, on_delete=PROTECT)

    report_datetime = models.DateTimeField(default=get_utcnow)

    f1 = models.CharField(max_length=50, null=True, blank=True)

    f2 = models.CharField(max_length=50, null=True, blank=True)

    f3 = models.CharField(max_length=50, null=True, blank=True)

    next_appt_date = models.DateField(null=True, blank=True)

    next_visit_code = models.CharField(max_length=50, null=True, blank=True)


class CrfTwo(CrfModelMixin, BaseUuidModel):
    subject_visit = models.ForeignKey(SubjectVisit, on_delete=PROTECT)

    report_datetime = models.DateTimeField(default=get_utcnow)

    f1 = models.CharField(max_length=50, null=True, blank=True)

    f2 = models.CharField(max_length=50, null=True, blank=True)

    f3 = models.CharField(max_length=50, null=True, blank=True)

    visitschedule = models.ForeignKey(
        VisitSchedule, on_delete=PROTECT, max_length=15, null=True, blank=False
    )


class CrfThree(CrfModelMixin, BaseUuidModel):
    subject_visit = models.ForeignKey(SubjectVisit, on_delete=PROTECT)

    report_datetime = models.DateTimeField(default=get_utcnow)

    f1 = models.CharField(max_length=50, null=True, blank=True)

    f2 = models.CharField(max_length=50, null=True, blank=True)

    f3 = models.CharField(max_length=50, null=True, blank=True)

    allow_create_interim = models.BooleanField(default=False)

    appt_date = models.DateField(null=True, blank=True)


class CrfFour(CrfModelMixin, BaseUuidModel):
    subject_visit = models.ForeignKey(SubjectVisit, on_delete=PROTECT)

    report_datetime = models.DateTimeField(default=get_utcnow)

    f1 = models.CharField(max_length=50, null=True, blank=True)

    f2 = models.CharField(max_length=50, null=True, blank=True)

    f3 = models.CharField(max_length=50, null=True, blank=True)


class CrfFive(CrfModelMixin, BaseUuidModel):
    subject_visit = models.ForeignKey(SubjectVisit, on_delete=PROTECT)

    report_datetime = models.DateTimeField(default=get_utcnow)

    f1 = models.CharField(max_length=50, null=True, blank=True)

    f2 = models.CharField(max_length=50, null=True, blank=True)

    f3 = models.CharField(max_length=50, null=True, blank=True)


class NextAppointmentCrf(NextAppointmentCrfModelMixin, CrfModelMixin, BaseUuidModel):
    subject_visit = models.ForeignKey(SubjectVisit, on_delete=PROTECT)
