from django.contrib import admin

from edc_appointment.admin import edc_appointment_admin
from example.models import Appointment, TestModel

edc_appointment_admin.register(Appointment)
admin.site.register(TestModel)
