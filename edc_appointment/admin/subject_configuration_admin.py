from django.contrib import admin

from .base_model_admin import BaseModelAdmin

from ..forms import SubjectConfigurationForm
from ..models import SubjectConfiguration


class SubjectConfigurationAdmin(BaseModelAdmin):
    form = SubjectConfigurationForm

    list_display = ('appointment_identifier', 'default_appt_type')
    search_fields = ('appointment_identifier', )
    list_filter = ('default_appt_type', )
admin.site.register(SubjectConfiguration, SubjectConfigurationAdmin)
