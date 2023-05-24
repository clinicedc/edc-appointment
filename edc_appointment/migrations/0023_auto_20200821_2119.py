# Generated by Django 3.0.9 on 2020-08-21 18:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("edc_appointment", "0022_auto_20200729_2310"),
    ]

    operations = [
        migrations.AlterField(
            model_name="appointment",
            name="appt_reason",
            field=models.CharField(
                choices=[
                    ("scheduled", "Scheduled visit (study)"),
                    ("unscheduled", "Routine / Unscheduled (non-study)"),
                ],
                help_text="The visit report's `reason for visit` will be validated against this. Refer to the protocol's documentation for the definition of a `scheduled` visit.",
                max_length=25,
                verbose_name="Reason for appointment",
            ),
        ),
        migrations.AlterField(
            model_name="appointment",
            name="appt_status",
            field=models.CharField(
                choices=[
                    ("new", "New"),
                    ("in_progress", "In Progress"),
                    ("incomplete", "Incomplete"),
                    ("done", "Done"),
                    ("cancelled", "Cancelled"),
                ],
                db_index=True,
                default="new",
                help_text="If the visit has already begun, only 'in progress', 'incomplete' or 'done' are valid options",
                max_length=25,
                verbose_name="Status",
            ),
        ),
        migrations.AlterField(
            model_name="historicalappointment",
            name="appt_reason",
            field=models.CharField(
                choices=[
                    ("scheduled", "Scheduled visit (study)"),
                    ("unscheduled", "Routine / Unscheduled (non-study)"),
                ],
                help_text="The visit report's `reason for visit` will be validated against this. Refer to the protocol's documentation for the definition of a `scheduled` visit.",
                max_length=25,
                verbose_name="Reason for appointment",
            ),
        ),
        migrations.AlterField(
            model_name="historicalappointment",
            name="appt_status",
            field=models.CharField(
                choices=[
                    ("new", "New"),
                    ("in_progress", "In Progress"),
                    ("incomplete", "Incomplete"),
                    ("done", "Done"),
                    ("cancelled", "Cancelled"),
                ],
                db_index=True,
                default="new",
                help_text="If the visit has already begun, only 'in progress', 'incomplete' or 'done' are valid options",
                max_length=25,
                verbose_name="Status",
            ),
        ),
    ]
