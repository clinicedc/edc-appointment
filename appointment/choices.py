from edc.constants import IN_PROGRESS, INCOMPLETE, DONE, CANCELLED
APPT_STATUS = (
    ('new', 'New'),
    (IN_PROGRESS, 'In Progress'),
    (INCOMPLETE, 'Incomplete'),
    (DONE, 'Done'),
    (CANCELLED, 'Cancelled'),
    )

APPT_TYPE = (
    ('clinic', 'In clinic'),
    ('telephone', 'By telephone'),
    ('home', 'At home'),
    )

INFO_PROVIDER = (
    ('subject', 'Subject'),
    ('other', 'Other person'),
)
