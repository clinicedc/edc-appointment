# Generated by Django 2.0.7 on 2018-07-06 13:19

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [("edc_appointment", "0014_auto_20180116_1411")]

    operations = [
        migrations.AlterModelOptions(
            name="historicalappointment",
            options={
                "get_latest_by": "history_date",
                "ordering": ("-history_date", "-history_id"),
                "verbose_name": "historical appointment",
            },
        )
    ]
