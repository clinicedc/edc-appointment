# Generated by Django 4.2.3 on 2023-08-16 15:25

from django.db import migrations
import edc_model_fields.fields.other_charfield


class Migration(migrations.Migration):
    dependencies = [
        ("edc_appointment", "0039_appointmenttype_extra_value"),
    ]

    operations = [
        migrations.AddField(
            model_name="appointment",
            name="appt_type_other",
            field=edc_model_fields.fields.other_charfield.OtherCharField(
                blank=True,
                max_length=35,
                null=True,
                verbose_name="If other appointment type, please specify ...",
            ),
        ),
        migrations.AddField(
            model_name="historicalappointment",
            name="appt_type_other",
            field=edc_model_fields.fields.other_charfield.OtherCharField(
                blank=True,
                max_length=35,
                null=True,
                verbose_name="If other appointment type, please specify ...",
            ),
        ),
    ]