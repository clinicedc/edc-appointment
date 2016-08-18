# from simple_history.models import HistoricalRecords

from edc_base.model.models.base_uuid_model import BaseUuidModel
from edc_registration.models import RegisteredSubjectModelMixin


class RegisteredSubject(RegisteredSubjectModelMixin, BaseUuidModel):

#     history = HistoricalRecords()

    class Meta:
        app_label = 'example_registration'
