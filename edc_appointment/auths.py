from edc_auth.site_auths import site_auths

from .auth_objects import APPOINTMENT, APPOINTMENT_EXPORT, APPOINTMENT_VIEW

site_auths.add_group(
    "edc_appointment.view_appointment",
    "edc_appointment.view_historicalappointment",
    name=APPOINTMENT_VIEW,
)

site_auths.add_group(
    "edc_appointment.add_appointment",
    "edc_appointment.change_appointment",
    "edc_appointment.view_appointment",
    "edc_appointment.view_historicalappointment",
    name=APPOINTMENT,
)

site_auths.add_group(
    "edc_appointment.export_appointment",
    name=APPOINTMENT_EXPORT,
)
