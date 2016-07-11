import factory

from django.utils import timezone

from example.models import Appointment


class AppointmentFactory(factory.DjangoModelFactory):

    class Meta:
        model = Appointment

    appt_datetime = timezone.now()
    visit_schedule_name = 'Example Visit Schedule'
    schedule_name = 'schedule-1'
    visit_code = '2000'
    visit_code_sequence = 0
    appt_type = 'clinic'
