from dateutil.relativedelta import relativedelta
from edc_visit_schedule import Schedule, Visit, VisitSchedule

from edc_appointment_app.visit_schedule.crfs import crfs, crfs_missed

visit_schedule4 = VisitSchedule(
    name="visit_schedule4",
    offstudy_model="edc_appointment_app.subjectoffstudy",
    death_report_model="edc_appointment_app.deathreport",
)

schedule4 = Schedule(
    name="three_monthly_schedule",
    onschedule_model="edc_appointment_app.onschedulethree",
    offschedule_model="edc_appointment_app.offschedulethree",
    appointment_model="edc_appointment.appointment",
    consent_model="edc_appointment_app.subjectconsent",
)

visits = [
    Visit(
        code="1000",
        title="Baseline",
        timepoint=0,
        rbase=relativedelta(days=0),
        rlower=relativedelta(days=0),
        rupper=relativedelta(days=0),
        add_window_gap_to_lower=True,
        requisitions=None,
        crfs=crfs,
        crfs_missed=crfs_missed,
        facility_name="7-day-clinic",
    )
]
for index, visit_code in [(3, "1030"), (6, "1060"), (9, "1090"), (12, "1120")]:
    visits.append(
        Visit(
            code=visit_code,
            title=f"Month {index}",
            timepoint=index,
            rbase=relativedelta(months=index),
            rlower=relativedelta(days=15),
            rupper=relativedelta(days=15),
            add_window_gap_to_lower=True,
            max_window_gap_to_lower=None,
            requisitions=None,
            crfs=crfs,
            crfs_missed=crfs_missed,
            facility_name="7-day-clinic",
            allow_unscheduled=True,
        )
    )
for visit in visits:
    schedule4.add_visit(visit)

visit_schedule4.add_schedule(schedule4)
