from django.db.models.signals import post_save
from django.dispatch import receiver
from .base_appointment_helper_model import BaseAppointmentHelperModel
from .base_appointment_mixin import BaseAppointmentMixin


@receiver(post_save, weak=False, dispatch_uid="prepare_appointments_on_post_save")
def prepare_appointments_on_post_save(sender, instance, raw, created, using, **kwargs):
    """"""
    if not raw:
        if issubclass(sender, (BaseAppointmentHelperModel, BaseAppointmentMixin)):
            instance.prepare_appointments(using)
