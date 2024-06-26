from edc_visit_schedule.tests.dummy_panel import DummyPanel
from edc_visit_schedule.visit import (
    Crf,
    CrfCollection,
    Requisition,
    RequisitionCollection,
)


class MockPanel(DummyPanel):
    """`requisition_model` is normally set when the lab profile
    is set up.
    """

    def __init__(self, name):
        super().__init__(requisition_model="edc_appointment_app.subjectrequisition", name=name)


panel_one = MockPanel(name="one")
panel_two = MockPanel(name="two")
panel_three = MockPanel(name="three")
panel_four = MockPanel(name="four")
panel_five = MockPanel(name="five")
panel_six = MockPanel(name="six")

crfs = CrfCollection(
    Crf(show_order=1, model="edc_appointment_app.crfone", required=True),
    Crf(show_order=2, model="edc_appointment_app.crftwo", required=True),
    Crf(show_order=3, model="edc_appointment_app.crfthree", required=True),
    Crf(show_order=4, model="edc_appointment_app.crffour", required=True),
    Crf(show_order=5, model="edc_appointment_app.crffive", required=True),
)

crfs_missed = CrfCollection(
    Crf(show_order=10, model="edc_appointment_app.subjectvisitmissed"),
    name="missed",
)

requisitions = RequisitionCollection(
    Requisition(show_order=10, panel=panel_one, required=True, additional=False),
    Requisition(show_order=20, panel=panel_two, required=True, additional=False),
    Requisition(show_order=30, panel=panel_three, required=True, additional=False),
    Requisition(show_order=40, panel=panel_four, required=True, additional=False),
    Requisition(show_order=50, panel=panel_five, required=True, additional=False),
    Requisition(show_order=60, panel=panel_six, required=True, additional=False),
)


crfs_unscheduled = CrfCollection(
    Crf(show_order=1, model="edc_appointment_app.crfone", required=True),
    Crf(show_order=3, model="edc_appointment_app.crfthree", required=True),
    Crf(show_order=5, model="edc_appointment_app.crffive", required=True),
)
