from django import forms
from edc_crf.crf_form_validator import CrfFormValidator
from edc_crf.modelform_mixins import CrfModelFormMixin
from edc_next_appointment.form_validators import NextAppointmentFormValidatorMixin
from edc_next_appointment.modelform_mixins import NextAppointmentModelFormMixin

from .models import CrfThree


class NextAppointmentFormValidator(NextAppointmentFormValidatorMixin, CrfFormValidator):
    def clean(self):
        self.validate_date_is_on_clinic_day()
        super().clean()


class CrfThreeForm(NextAppointmentModelFormMixin, CrfModelFormMixin, forms.ModelForm):
    form_validator_cls = NextAppointmentFormValidator

    appt_date_fld = "appt_date"
    visit_code_fld = "f1"

    def validate_against_consent(self) -> None:
        pass

    class Meta:
        model = CrfThree
        fields = "__all__"
        labels = {"appt_date": "Next scheduled appointment date"}
