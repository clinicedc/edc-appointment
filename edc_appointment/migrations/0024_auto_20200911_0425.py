# Generated by Django 3.0.9 on 2020-09-11 01:25

import edc_sites.models
from django.db import migrations

import edc_appointment.managers


class Migration(migrations.Migration):
    dependencies = [
        ("edc_appointment", "0023_auto_20200821_2119"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="appointment",
            managers=[
                ("on_site", edc_sites.models.CurrentSiteManager()),
                ("objects", edc_appointment.managers.AppointmentManager()),
            ],
        ),
    ]
