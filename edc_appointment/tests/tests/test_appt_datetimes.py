from datetime import datetime
from zoneinfo import ZoneInfo

import time_machine
from dateutil._common import weekday
from dateutil.relativedelta import FR, MO, SA, SU, TH, TU, WE, relativedelta
from django.test import TestCase, override_settings
from edc_consent.site_consents import site_consents
from edc_facility.import_holidays import import_holidays
from edc_visit_schedule.schedule.visit_collection import VisitCollection
from edc_visit_schedule.site_visit_schedules import site_visit_schedules

from edc_appointment.models import Appointment
from edc_appointment_app.consents import consent_v1
from edc_appointment_app.visit_schedule import get_visit_schedule1

from ..helper import Helper

utc_tz = ZoneInfo("UTC")


@override_settings(SITE_ID=10)
@time_machine.travel(datetime(2019, 6, 11, 8, 00, tzinfo=utc_tz))
class TestApptDatetimes(TestCase):
    helper_cls = Helper

    """Note: visit schedule has appointments on days 0, 1, 2, 3, etc.
    Default facility accepts appointments any day of the week.
    """

    @classmethod
    def setUpTestData(cls):
        import_holidays()
        site_consents.registry = {}
        site_consents.register(consent_v1)

    def register_visit_schedule(self, facility_name=None):
        """Overwrite facility name on each visit and register
        the modified visit_schedule.
        """
        visit_schedule = get_visit_schedule1()
        for schedule_name, schedule in visit_schedule.schedules.items():
            visit_collection = VisitCollection()
            for k, v in schedule.visits.items():
                v.facility_name = facility_name
                visit_collection.update({k: v})
            schedule._visits = visit_collection
            visit_schedule.schedules[schedule_name] = schedule
        site_visit_schedules._registry = {}
        site_visit_schedules.register(visit_schedule=visit_schedule)
        visit_schedule = site_visit_schedules.get_visit_schedule(visit_schedule.name)
        for schedule_name, schedule in visit_schedule.schedules.items():
            for k, v in schedule.visits.items():
                self.assertEqual(v.facility_name, facility_name)

    def get_appt_datetimes(self, base_appt_datetime=None, subject_identifier=None):
        self.assertIsNotNone(base_appt_datetime)
        now = base_appt_datetime.astimezone(ZoneInfo("UTC"))
        self.helper = self.helper_cls(subject_identifier=subject_identifier, now=now)
        self.helper.consent_and_put_on_schedule(
            visit_schedule_name="visit_schedule1", schedule_name="schedule1"
        )
        appointments = Appointment.objects.filter(subject_identifier=subject_identifier)
        return [obj.appt_datetime for obj in appointments]

    def test_appointments_creation_dates(self):
        """Assert does not skip any days regardless of
        base appointment day.

        default facility (in tests) accepts appointments any day
        of the week.
        """
        self.register_visit_schedule(facility_name="7-day-clinic")
        for i in range(0, 7, 7):
            subject_identifier = f"12345{i}"
            dte = datetime(2017, 1, 7) + relativedelta(days=i)
            now = dte.astimezone(ZoneInfo("UTC"))
            self.helper = self.helper_cls(subject_identifier=subject_identifier, now=now)
            self.helper.consent_and_put_on_schedule(
                visit_schedule_name="visit_schedule1", schedule_name="schedule1"
            )
            appointments = Appointment.objects.filter(subject_identifier=subject_identifier)
            appt_datetimes = [obj.appt_datetime for obj in appointments]
            base_appt_datetime = appt_datetimes[0]
            for index, appt_datetime in enumerate(appt_datetimes):
                self.assertEqual(
                    base_appt_datetime + relativedelta(days=index * 7), appt_datetime
                )

    def test_appointments_creation_dates2(self):
        """Assert skips SA, SU."""
        self.register_visit_schedule(facility_name="5-day-clinic")
        base_appt_datetime = datetime(2017, 1, 7)  # noqa
        self.assertTrue(weekday(base_appt_datetime.weekday()), SA)
        appt_datetimes = self.get_appt_datetimes(
            base_appt_datetime=base_appt_datetime, subject_identifier="123456"
        )
        self.assertTrue(weekday(appt_datetimes[0].weekday()), MO)
        self.assertTrue(weekday(appt_datetimes[1].weekday()), TU)
        self.assertTrue(weekday(appt_datetimes[2].weekday()), WE)
        self.assertTrue(weekday(appt_datetimes[3].weekday()), TH)

    def test_appointments_creation_dates3(self):
        """Assert skips SA, SU."""
        self.register_visit_schedule(facility_name="5-day-clinic")
        base_appt_datetime = datetime(2017, 1, 8)
        self.assertTrue(weekday(base_appt_datetime.weekday()), SU)
        appt_datetimes = self.get_appt_datetimes(
            base_appt_datetime=base_appt_datetime, subject_identifier="1234567"
        )
        self.assertTrue(weekday(appt_datetimes[0].weekday()), MO)
        self.assertTrue(weekday(appt_datetimes[1].weekday()), TU)
        self.assertTrue(weekday(appt_datetimes[2].weekday()), WE)
        self.assertTrue(weekday(appt_datetimes[3].weekday()), TH)

    def test_appointments_creation_dates4(self):
        """Assert skips SA, SU."""
        self.register_visit_schedule(facility_name="5-day-clinic")
        base_appt_datetime = datetime(2017, 1, 9)
        self.assertTrue(weekday(base_appt_datetime.weekday()), MO)
        appt_datetimes = self.get_appt_datetimes(
            base_appt_datetime=base_appt_datetime, subject_identifier="12345678"
        )
        self.assertTrue(weekday(appt_datetimes[0].weekday()), MO)
        self.assertTrue(weekday(appt_datetimes[1].weekday()), TU)
        self.assertTrue(weekday(appt_datetimes[2].weekday()), WE)
        self.assertTrue(weekday(appt_datetimes[3].weekday()), TH)

    def test_appointments_creation_dates5(self):
        """Assert skips SA, SU."""
        self.register_visit_schedule(facility_name="5-day-clinic")
        base_appt_datetime = datetime(2017, 1, 10)
        self.assertTrue(weekday(base_appt_datetime.weekday()), TU)
        appt_datetimes = self.get_appt_datetimes(
            base_appt_datetime=base_appt_datetime, subject_identifier="123456789"
        )
        self.assertTrue(weekday(appt_datetimes[0].weekday()), TU)
        self.assertTrue(weekday(appt_datetimes[1].weekday()), WE)
        self.assertTrue(weekday(appt_datetimes[2].weekday()), TH)
        self.assertTrue(weekday(appt_datetimes[3].weekday()), FR)

    def test_appointments_creation_dates6(self):
        """Assert skips SA, SU."""
        self.register_visit_schedule(facility_name="5-day-clinic")
        base_appt_datetime = datetime(2017, 1, 11)
        self.assertTrue(weekday(base_appt_datetime.weekday()), WE)
        appt_datetimes = self.get_appt_datetimes(
            base_appt_datetime=base_appt_datetime, subject_identifier="1234567890"
        )
        self.assertTrue(weekday(appt_datetimes[0].weekday()), WE)
        self.assertTrue(weekday(appt_datetimes[1].weekday()), TH)
        self.assertTrue(weekday(appt_datetimes[2].weekday()), FR)
        self.assertTrue(weekday(appt_datetimes[3].weekday()), MO)

    def test_appointments_creation_dates7(self):
        """Assert 3-day-clinic skips FR, SA, SU, MO."""
        self.register_visit_schedule(facility_name="3-day-clinic")
        base_appt_datetime = datetime(2017, 1, 7)  # noqa
        self.assertTrue(weekday(base_appt_datetime.weekday()), SA)
        appt_datetimes = self.get_appt_datetimes(
            base_appt_datetime=base_appt_datetime, subject_identifier="123456"
        )
        self.assertTrue(weekday(appt_datetimes[0].weekday()), TU)
        self.assertTrue(weekday(appt_datetimes[1].weekday()), WE)
        self.assertTrue(weekday(appt_datetimes[2].weekday()), TH)
        self.assertTrue(weekday(appt_datetimes[3].weekday()), TU)

    def test_appointments_creation_dates8(self):
        """Assert 3-day-clinic skips FR, SA, SU, MO."""
        self.register_visit_schedule(facility_name="3-day-clinic")
        base_appt_datetime = datetime(2017, 1, 8)
        self.assertTrue(weekday(base_appt_datetime.weekday()), SU)
        appt_datetimes = self.get_appt_datetimes(
            base_appt_datetime=base_appt_datetime, subject_identifier="1234567"
        )
        self.assertTrue(weekday(appt_datetimes[0].weekday()), TU)
        self.assertTrue(weekday(appt_datetimes[1].weekday()), WE)
        self.assertTrue(weekday(appt_datetimes[2].weekday()), TH)
        self.assertTrue(weekday(appt_datetimes[3].weekday()), TU)

    def test_appointments_creation_dates9(self):
        """Assert 3-day-clinic skips FR, SA, SU, MO."""
        self.register_visit_schedule(facility_name="3-day-clinic")
        base_appt_datetime = datetime(2017, 1, 9)
        self.assertTrue(weekday(base_appt_datetime.weekday()), MO)
        appt_datetimes = self.get_appt_datetimes(
            base_appt_datetime=base_appt_datetime, subject_identifier="12345678"
        )
        self.assertTrue(weekday(appt_datetimes[0].weekday()), TU)
        self.assertTrue(weekday(appt_datetimes[1].weekday()), WE)
        self.assertTrue(weekday(appt_datetimes[2].weekday()), TH)
        self.assertTrue(weekday(appt_datetimes[3].weekday()), TU)

    def test_appointments_creation_dates10(self):
        """Assert 3-day-clinic skips FR, SA, SU, MO."""
        self.register_visit_schedule(facility_name="3-day-clinic")
        base_appt_datetime = datetime(2017, 1, 10)
        self.assertTrue(weekday(base_appt_datetime.weekday()), TU)
        appt_datetimes = self.get_appt_datetimes(
            base_appt_datetime=base_appt_datetime, subject_identifier="123456789"
        )
        self.assertTrue(weekday(appt_datetimes[0].weekday()), TU)
        self.assertTrue(weekday(appt_datetimes[1].weekday()), WE)
        self.assertTrue(weekday(appt_datetimes[2].weekday()), TH)
        self.assertTrue(weekday(appt_datetimes[3].weekday()), TU)

    def test_appointments_creation_dates11(self):
        """Assert 3-day-clinic skips FR, SA, SU, MO."""
        self.register_visit_schedule(facility_name="3-day-clinic")
        base_appt_datetime = datetime(2017, 1, 11)
        self.assertTrue(weekday(base_appt_datetime.weekday()), WE)
        appt_datetimes = self.get_appt_datetimes(
            base_appt_datetime=base_appt_datetime, subject_identifier="1234567890"
        )
        self.assertTrue(weekday(appt_datetimes[0].weekday()), WE)
        self.assertTrue(weekday(appt_datetimes[1].weekday()), TH)
        self.assertTrue(weekday(appt_datetimes[2].weekday()), FR)
        self.assertTrue(weekday(appt_datetimes[3].weekday()), TU)
