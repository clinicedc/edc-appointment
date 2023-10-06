from django import forms
from edc_crf.crf_form_validator import CrfFormValidator
from edc_crf.modelform_mixins import CrfModelFormMixin

from edc_appointment.form_validator_mixins import NextAppointmentCrfFormValidatorMixin
from edc_appointment.modelform_mixins import NextAppointmentCrfModelFormMixin

from .models import CrfThree, NextAppointmentCrf


class NextAppointmentCrfFormValidator(NextAppointmentCrfFormValidatorMixin, CrfFormValidator):
    def clean(self):
        self.validate_date_is_on_clinic_day()
        super().clean()


class CrfThreeForm(NextAppointmentCrfModelFormMixin, CrfModelFormMixin, forms.ModelForm):
    form_validator_cls = NextAppointmentCrfFormValidator

    appt_date_fld = "appt_date"
    visit_code_fld = "f1"

    def validate_against_consent(self) -> None:
        pass

    class Meta:
        model = CrfThree
        fields = "__all__"
        labels = {"appt_date": "Next scheduled appointment date"}


class NextAppointmentCrfForm(
    NextAppointmentCrfModelFormMixin, CrfModelFormMixin, forms.ModelForm
):
    form_validator_cls = NextAppointmentCrfFormValidator

    def validate_against_consent(self) -> None:
        pass

    class Meta:
        model = NextAppointmentCrf
        fields = "__all__"
