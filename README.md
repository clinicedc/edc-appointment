[![Build Status](https://travis-ci.org/botswana-harvard/edc-appointment.svg?branch=develop)](https://travis-ci.org/botswana-harvard/edc-appointment) [![Coverage Status](https://coveralls.io/repos/botswana-harvard/edc-appointment/badge.svg?branch=develop&service=github)](https://coveralls.io/github/botswana-harvard/edc-appointment?branch=develop)

# edc-appointment

This module works closely with `edc_visit_tracking` and `edc_visit_schedule`.

In a research protocol participant data is collected on a predefined visit schedule. The visit schedule is defined in `edc-visit-schedul`. `edc-appointment` creates appointments for participants based the selected visit schedule.

### `AppointmentModelMixin`

A model mixin for the Appointment model. Each project may have one appointment model. For example:

    class Appointment(AppointmentModelMixin, RequiresConsentMixin, BaseUuidModel):
    
        class Meta(AppointmentModelMixin.Meta):
            consent_model = 'edc_example.subjectconsent'
            app_label = 'edc_example'


### `CreatesAppointmentsModelMixin`

A model mixin for the model that triggers the creation of appointments when the model is saved. This is typically an enrollment model.

Adds the model field `facility`. The value of field `facility` tells the `CreateAppointmentsMixin` to create appointments for the subject on dates that are available at the `facility`.

    class Enrollment(EnrollmentModelMixin, CreateAppointmentsMixin, RequiresConsentMixin, BaseUuidModel):
    
        class Meta(EnrollmentModelMixin.Meta):
            visit_schedule_name = 'subject_visit_schedule.schedule1'
            consent_model = 'edc_example.subjectconsent'
            app_label = 'edc_example'

When `Enrollment` declared above is saved, one appointment will be created for the subject for each `visit` in schedule `schedule1` of visit_schedule `subject_visit_schedule`. 

Note: the value for `facility` must be provided by the user, either through the form interface or programmatically. 

### Customizing appointment scheduling by `Facility`

Appointment scheduling can be customized per `facility` or clinic:

Add each facility to `app_config.facilities` specifying the facility `name`, `days` open and the maximum number of `slots` available per day:

    from edc_appointment.apps import AppConfig as EdcAppointmentAppConfig

    class AppConfig(EdcAppointmentAppConfig):

        facilities = {
            'clinic1': Facility(name='clinic', days=[MO, TU, WE, TH, FR], slots=[100, 100, 100, 100, 100])}
            'clinic2': Facility(name='clinic', days=[MO, WE, FR], slots=[30, 30, 30])}

To schedule an appointment that falls on a day that the clinic is open, isn't a holiday and isn't already over-booked:

    from django.utils import timezone
    from .facility import Facility
    
    suggested_datetime = timezone.now()
    available_datetime = facility.available_datetime(suggested_datetime)


If holidays are entered (in model `Holiday`) and the appointment lands on a holiday, the appointment date is incremented forward to an allowed weekday. Assuming `facility` is configured in `app_config` to only schedule appointments on [TU, TH]:

    from datetime import datetime
    from dateutil.relativedelta import TU, TH
    from django.conf import settings
    from django.utils import timezone

    from .facility import Facility
    from .models import Holiday
    
    Holiday.objects.create(
        name='Id-ul-Adha (Feast of the Sacrifice)',
        date=date(2015, 9, 24)
    )
    suggested_datetime = timezone.make_aware(datetime(2015, 9, 24), timezone=pytz.timezone('UTC'))  # TH
    available_datetime = facility.available_datetime(suggested_datetime)
    print(available_datetime)  # 2015-09-29 00:00:00, TU

The maximum number of possible scheduling slots per day is configured in `app_config`. As with the holiday example above, the appointment date will be incremented forward to a day with an available slot.


### Available Appointment Model Manager Methods

The `Appointment` model is declared with `AppointmentManager`. It has several useful methods. 

#### `first_appointment()`, `last_appointment()`

Returns the first (or last) appointment. If just the `subject_identifier` is provided, the first appointment of the protocol for the subject is returned. To be more specific, provide `{subject_identifier=subject_identifier, visit_schedule_name=visit_schedule_name}`.
To be even more specific,  `{subject_identifier=subject_identifier, visit_schedule_name=visit_schedule_name, schedule_name=schedule_name}`.

The most common usage is to just provide these values with an appointment instance:

    first_appointment = Appointment.objects.first_appointment(appointment=appointment)

#### `next_appointment()`, `previous_appointment()`

The next and previous appointment are relative to the schedule and a visit_code within that schedule. If next is called on the last appointment in the sequence `None` is returned. If previous is called on the first appointment in the sequence `None` is returned.

For example, in a sequence of appointment 1000, 2000, 3000, 4000:

    >>> appointment.visit_code
    1000
    >>> next_appointment = Appointment.objects.next_appointment(appointment=appointment)
    >>> next_appointment.visit_code
    2000

But you can also pass an appointment instance and pass the visit code:

    >>> appointment.visit_code
    1000
    >>> next_appointment = Appointment.objects.next_appointment(appointment=appointment, visit_code=3000)
    >>> next_appointment.visit_code
    4000
If you ask for the next appointment from the last, `None` is returned:

    >>> appointment.visit_code
    4000
    >>> next_appointment = Appointment.objects.next_appointment(appointment=appointment, visit_code=3000)
    >>> next_appointment.visit_code
    AttributeError: 'NoneType' object has no attribute 'visit_code'

The `previous_appointment` acts as expected:

    >>> appointment.visit_code
    1000
    >>> previous_appointment = Appointment.objects.previous_appointment(appointment=appointment)
    >>> previous_appointment.visit_code
    AttributeError: 'NoneType' object has no attribute 'visit_code'



