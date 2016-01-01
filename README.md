[![Build Status](https://travis-ci.org/botswana-harvard/edc-appointment.svg?branch=develop)](https://travis-ci.org/botswana-harvard/edc-appointment) [![Coverage Status](https://coveralls.io/repos/botswana-harvard/edc-appointment/badge.svg?branch=develop&service=github)](https://coveralls.io/github/botswana-harvard/edc-appointment?branch=develop)

# edc-appointment

In a research protocol, data is collected from participants on a fix schedule of visits. This module
creates appointments for participant visits when given a visit schedule (from edc_visit_scedule).

* appointments are created for each timepoint on the data collection schedule; 
* appointments are created when a special form is completed;
* the special form can be a registration form, consent or eligibility checklist that uses the
appointment mixin;
* a participant may "register" to more than one cohort linked to data collection schedule by having more than
one registration form using the mixin; 
* data management can "close" a timepoint to prevent further modification using the TimePointStatus model
and mixin.
