[![Build Status](https://travis-ci.org/botswana-harvard/edc-appointment.svg?branch=develop)](https://travis-ci.org/botswana-harvard/edc-appointment) [![Coverage Status](https://coveralls.io/repos/botswana-harvard/edc-appointment/badge.svg?branch=develop&service=github)](https://coveralls.io/github/botswana-harvard/edc-appointment?branch=develop)

# edc-appointment

This works closely with `edc_visit_tracking` and `edc_visit_schedule`.

As per a research protocol, participant data is collected on a predefined schedule. This module
creates appointments for participant visits when given a visit schedule (from edc_visit_scedule).

* appointments are created for each timepoint of the data collection schedule; 
* appointments are created by forms that use the `AppointmentMixin`, for example a registration form, consent or eligibility checklist;
* a participant may "register" to more than one cohort linked to data collection schedule by having more than
one registration form using the mixin; 
* The `TimePointStatusMixin` detects when data covered by an appointment is open or clsed for further editing.

### `AppointmentMixin`

Creates Appointments

Deletes Appointments


