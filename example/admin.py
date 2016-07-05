from django.contrib import admin
from example.models import RegisteredSubject, Appointment, TestModel, CrfMetaData, RequisitionMetaData
from edc_appointment.admin import edc_appointment_admin
from edc_meta_data.admin import edc_meta_data_admin

edc_appointment_admin.register(Appointment)
edc_meta_data_admin.register(CrfMetaData)
edc_meta_data_admin.register(RequisitionMetaData)
admin.site.register(RegisteredSubject)
admin.site.register(TestModel)
