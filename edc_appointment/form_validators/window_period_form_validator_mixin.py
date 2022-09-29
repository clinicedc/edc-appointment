from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from django.conf import settings
from edc_utils import convert_php_dateformat
from edc_visit_schedule.schedule.window import (
    ScheduledVisitWindowError,
    UnScheduledVisitWindowError,
)

from edc_appointment.constants import COMPLETE_APPT, INCOMPLETE_APPT

if TYPE_CHECKING:
    from edc_appointment.models import Appointment

UNSCHEDULED_WINDOW_ERROR = "unscheduled_window_error"
SCHEDULED_WINDOW_ERROR = "scheduled_window_error"


class WindowPeriodFormValidatorMixin:
    def validate_appt_datetime_in_window_period(self, appointment: Appointment, *args) -> None:
        self.datetime_in_window_or_raise(appointment, *args)

    def validate_visit_datetime_in_window_period(self, *args) -> None:
        self.datetime_in_window_or_raise(*args)

    def validate_crf_datetime_in_window_period(self, *args) -> None:
        self.datetime_in_window_or_raise(*args)

    @staticmethod
    def ignore_window_period_for_unscheduled(
        appointment: Appointment, proposed_appt_datetime: datetime
    ) -> bool:
        value = False
        if (
            appointment
            and appointment.visit_code_sequence > 0
            and appointment.next
            and appointment.next.appt_status in [INCOMPLETE_APPT, COMPLETE_APPT]
            and proposed_appt_datetime < appointment.next.appt_datetime
        ):
            value = True
        return value

    def datetime_in_window_or_raise(
        self,
        appointment: Appointment,
        proposed_appt_datetime: datetime,
        form_field: str,
    ):
        if proposed_appt_datetime:
            datetimestring = convert_php_dateformat(settings.SHORT_DATETIME_FORMAT)
            appointment.visit_from_schedule.timepoint_datetime = appointment.timepoint_datetime
            lower = appointment.visit_from_schedule.dates.lower.strftime(datetimestring)
            try:
                appointment.schedule.datetime_in_window(
                    timepoint_datetime=appointment.timepoint_datetime,
                    dt=proposed_appt_datetime,
                    visit_code=appointment.visit_code,
                    visit_code_sequence=appointment.visit_code_sequence,
                    baseline_timepoint_datetime=self.baseline_timepoint_datetime(appointment),
                )
            except UnScheduledVisitWindowError as e:
                if not self.ignore_window_period_for_unscheduled(
                    appointment, proposed_appt_datetime
                ):
                    upper = appointment.schedule.visits.next(
                        appointment.visit_code
                    ).dates.lower.strftime(datetimestring)
                    self.raise_validation_error(
                        {
                            form_field: (
                                "Invalid. Expected a date/time between "
                                f"{lower} and {upper} (U). Got {e}."
                            )
                        },
                        UNSCHEDULED_WINDOW_ERROR,
                    )
            except ScheduledVisitWindowError:
                upper = appointment.visit_from_schedule.dates.upper.strftime(datetimestring)
                proposed = proposed_appt_datetime.strftime(datetimestring)
                self.raise_validation_error(
                    {
                        form_field: (
                            f"Invalid. Expected a date/time between {lower} and {upper} (S). "
                            f"Got {proposed}."
                        )
                    },
                    SCHEDULED_WINDOW_ERROR,
                )

    @staticmethod
    def baseline_timepoint_datetime(appointment: Appointment) -> datetime:
        return appointment.__class__.objects.first_appointment(
            subject_identifier=appointment.subject_identifier,
            visit_schedule_name=appointment.visit_schedule_name,
            schedule_name=appointment.schedule_name,
        ).timepoint_datetime
