# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-25 06:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Holiday",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("day", models.DateField(unique=True)),
                ("name", models.CharField(blank=True, max_length=25, null=True)),
            ],
            options={"ordering": ["day"]},
        )
    ]
