# Generated by Django 3.2.13 on 2022-10-04 03:29

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("edc_appointment", "0031_auto_20220704_1841"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="appointment",
            unique_together={
                (
                    "subject_identifier",
                    "visit_schedule_name",
                    "schedule_name",
                    "appt_datetime",
                ),
                (
                    "subject_identifier",
                    "visit_schedule_name",
                    "schedule_name",
                    "visit_code",
                    "timepoint",
                    "visit_code_sequence",
                ),
            },
        ),
    ]
