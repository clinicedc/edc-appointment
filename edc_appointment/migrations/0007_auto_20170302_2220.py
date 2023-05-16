# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-02 20:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("edc_appointment", "0006_auto_20170106_2118")]

    operations = [
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
                help_text="If the visit has already begun, only 'in progress' or 'incomplete' are valid options",
                max_length=25,
                verbose_name="Status",
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
                help_text="If the visit has already begun, only 'in progress' or 'incomplete' are valid options",
                max_length=25,
                verbose_name="Status",
            ),
        ),
    ]
