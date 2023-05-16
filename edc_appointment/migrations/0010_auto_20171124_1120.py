# Generated by Django 2.0rc1 on 2017-11-24 09:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("edc_appointment", "0009_auto_20171119_1032")]

    operations = [
        migrations.AlterField(
            model_name="appointment",
            name="facility_name",
            field=models.CharField(
                help_text="set by model that creates appointments, e.g. Enrollment",
                max_length=25,
            ),
        ),
        migrations.AlterField(
            model_name="historicalappointment",
            name="facility_name",
            field=models.CharField(
                help_text="set by model that creates appointments, e.g. Enrollment",
                max_length=25,
            ),
        ),
    ]
