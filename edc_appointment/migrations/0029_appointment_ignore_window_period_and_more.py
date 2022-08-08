# Generated by Django 4.0.4 on 2022-05-26 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("edc_appointment", "0028_appointment_document_status_comments_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="appointment",
            name="ignore_window_period",
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AddField(
            model_name="historicalappointment",
            name="ignore_window_period",
            field=models.BooleanField(default=False, editable=False),
        ),
    ]
