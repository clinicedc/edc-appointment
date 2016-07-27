from edc_visit_schedule.site_visit_schedules import site_visit_schedules
from edc_visit_schedule.visit_schedule import VisitSchedule
from edc_visit_schedule.visit import Crf, Requisition

from example.models import TestModel, SubjectVisit

crfs = (
    Crf(show_order=10, app_label='example', model_name='CrfOne'),
    Crf(show_order=20, app_label='example', model_name='CrfTwo'),
)

requisitions = (
    Requisition(
        show_order=10, app_label='example', model_name='RequisitionOne',
        panel_name='Research Blood Draw', panel_type='TEST', aliqout_type_alpha_code='WB'),
)

example_visit_schedule = VisitSchedule(
    name='Example Visit Schedule',
    app_label='example',
)

# add schedules
example_visit_schedule.add_schedule(schedule_name='schedule-1', grouping_key='schedule-1')

# add membership form for this schedule
example_visit_schedule.add_membership_form(schedule_name='schedule-1', model=TestModel, visible=True)

# add visits to this schedule
example_visit_schedule.add_visit(
    code='1000',
    title='Visit 1000',
    schedule_name='schedule-1',
    time_point=0,
    base_interval=0,
    visit_model=SubjectVisit,
    requisitions=requisitions,
    crfs=crfs)
example_visit_schedule.add_visit(
    code='2000',
    title='Visit 2000',
    schedule_name='schedule-1',
    time_point=1,
    base_interval=1,
    visit_model=SubjectVisit,
    requisitions=requisitions,
    crfs=crfs)

# register the visit_schedule
site_visit_schedules.register(example_visit_schedule)
