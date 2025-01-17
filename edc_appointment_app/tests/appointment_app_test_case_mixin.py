from typing import Type

from edc_consent import site_consents
from edc_protocol.research_protocol_config import ResearchProtocolConfig
from edc_visit_schedule.site_visit_schedules import site_visit_schedules
from edc_visit_tracking.constants import SCHEDULED

from edc_appointment.constants import INCOMPLETE_APPT
from edc_appointment.creators import UnscheduledAppointmentCreator
from edc_appointment.models import Appointment
from edc_appointment_app.consents import consent_v1
from edc_appointment_app.models import SubjectVisit
from edc_appointment_app.visit_schedule import get_visit_schedule1, get_visit_schedule2


class AppointmentAppTestCaseMixin:
    helper_cls = None

    def setUp(self):
        super().setUp()

        self.subject_identifier = "12345"
        site_visit_schedules._registry = {}
        self.visit_schedule1 = get_visit_schedule1()
        self.visit_schedule2 = get_visit_schedule2()
        site_visit_schedules.register(self.visit_schedule1)
        site_visit_schedules.register(self.visit_schedule2)
        site_consents.registry = {}
        site_consents.register(consent_v1)
        self.helper = self.helper_cls(
            subject_identifier=self.subject_identifier,
            now=ResearchProtocolConfig().study_open_datetime,
        )
        self.helper.consent_and_put_on_schedule(
            visit_schedule_name=self.visit_schedule1.name, schedule_name="schedule1"
        )
        appointments = Appointment.objects.filter(subject_identifier=self.subject_identifier)
        self.assertEqual(appointments.count(), 4)

        appointment = Appointment.objects.get(timepoint=0.0)
        self.create_related_visit(appointment)
        self.create_unscheduled_appointments(appointment)

        self.appt_datetimes = [
            o.appt_datetime for o in Appointment.objects.all().order_by("appt_datetime")
        ]

    def create_unscheduled_appointments(self, appointment):
        for i in range(0, 3):
            creator = UnscheduledAppointmentCreator(
                subject_identifier=self.subject_identifier,
                visit_schedule_name=self.visit_schedule1.name,
                schedule_name="schedule1",
                visit_code="1000",
                suggested_visit_code_sequence=appointment.visit_code_sequence + 1,
            )
            appointment = creator.appointment
            appointment.appt_status = INCOMPLETE_APPT
            appointment.save_base(update_fields=["appt_status"])

    def create_related_visit(
        self, appointment: Appointment, reason: str | None = None
    ) -> SubjectVisit:
        if not appointment.related_visit:
            related_visit = SubjectVisit.objects.create(
                appointment=appointment,
                subject_identifier=appointment.subject_identifier,
                report_datetime=appointment.appt_datetime,
                visit_schedule_name=appointment.visit_schedule_name,
                schedule_name=appointment.schedule_name,
                visit_code=appointment.visit_code,
                visit_code_sequence=appointment.visit_code_sequence,
                reason=reason or SCHEDULED,
            )
            appointment.appt_status = INCOMPLETE_APPT
            appointment.save_base(update_fields=["appt_status"])
            appointment.refresh_from_db()
        else:
            related_visit = appointment.related_visit
        return related_visit

    @staticmethod
    def get_visit_codes(model_cls: Type[Appointment | SubjectVisit], order_by: str = None):
        return [
            f"{o.visit_code}.{o.visit_code_sequence}"
            for o in model_cls.objects.all().order_by(order_by)
        ]
