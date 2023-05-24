# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-26 11:56
from __future__ import unicode_literals

import django.core.validators
import django.db.models.deletion
import django_audit_fields.fields.uuid_auto_field
import django_extensions.db.fields
import django_revision.revision_field
import edc_model_fields.fields.hostname_modification_field
import edc_model_fields.fields.userfield
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("edc_appointment", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Appointment",
            fields=[
                (
                    "created",
                    django_extensions.db.fields.CreationDateTimeField(
                        auto_now_add=True, verbose_name="created"
                    ),
                ),
                (
                    "modified",
                    django_extensions.db.fields.ModificationDateTimeField(
                        auto_now=True, verbose_name="modified"
                    ),
                ),
                (
                    "user_created",
                    edc_model_fields.fields.userfield.UserField(
                        blank=True,
                        editable=False,
                        max_length=50,
                        verbose_name="user created",
                    ),
                ),
                (
                    "user_modified",
                    edc_model_fields.fields.userfield.UserField(
                        blank=True,
                        editable=False,
                        max_length=50,
                        verbose_name="user modified",
                    ),
                ),
                (
                    "hostname_created",
                    models.CharField(
                        default="mac2-2.local",
                        editable=False,
                        help_text="System field. (modified on create only)",
                        max_length=50,
                    ),
                ),
                (
                    "hostname_modified",
                    edc_model_fields.fields.hostname_modification_field.HostnameModificationField(
                        blank=True,
                        editable=False,
                        help_text="System field. (modified on every save)",
                        max_length=50,
                    ),
                ),
                (
                    "revision",
                    django_revision.revision_field.RevisionField(
                        blank=True,
                        editable=False,
                        help_text="System field. Git repository tag:branch:commit.",
                        max_length=75,
                        null=True,
                        verbose_name="Revision",
                    ),
                ),
                (
                    "id",
                    django_audit_fields.fields.uuid_auto_field.UUIDAutoField(
                        blank=True,
                        editable=False,
                        help_text="System auto field. UUID primary key.",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "subject_identifier",
                    models.CharField(
                        editable=False, max_length=50, verbose_name="Subject Identifier"
                    ),
                ),
                (
                    "timepoint_status",
                    models.CharField(
                        choices=[
                            ("open", "Open"),
                            ("feedback", "Feedback"),
                            ("closed", "Closed"),
                        ],
                        default="open",
                        max_length=15,
                    ),
                ),
                (
                    "timepoint_opened_datetime",
                    models.DateTimeField(
                        editable=False,
                        help_text="the original calculated model's datetime, updated in the signal",
                        null=True,
                    ),
                ),
                (
                    "timepoint_closed_datetime",
                    models.DateTimeField(editable=False, null=True),
                ),
                (
                    "visit_schedule_name",
                    models.CharField(
                        editable=False,
                        help_text='the name of the visit schedule used to find the "schedule"',
                        max_length=25,
                    ),
                ),
                ("schedule_name", models.CharField(editable=False, max_length=25)),
                (
                    "visit_code",
                    models.CharField(editable=False, max_length=25, null=True),
                ),
                (
                    "timepoint",
                    models.DecimalField(
                        decimal_places=1,
                        editable=False,
                        help_text="timepoint from schedule",
                        max_digits=6,
                        null=True,
                    ),
                ),
                (
                    "timepoint_datetime",
                    models.DateTimeField(
                        editable=False,
                        help_text="Unadjusted datetime calculated from visit schedule",
                        null=True,
                    ),
                ),
                (
                    "appt_close_datetime",
                    models.DateTimeField(
                        editable=False,
                        help_text="timepoint_datetime adjusted according to the nearest available datetime for this facility",
                        null=True,
                    ),
                ),
                ("facility_name", models.CharField(max_length=25)),
                (
                    "visit_instance",
                    models.CharField(
                        blank=True,
                        db_index=True,
                        default="0",
                        help_text="A decimal to represent an additional report to be included with the original visit report. (NNNN.0)",
                        max_length=1,
                        null=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                "[0-9]", "Must be a number from 0-9"
                            )
                        ],
                        verbose_name="Instance",
                    ),
                ),
                (
                    "visit_code_sequence",
                    models.IntegerField(
                        blank=True,
                        default=0,
                        help_text="An integer to represent the sequence of additional appointments relative to the base appointment, 0, needed to complete data collection for the timepoint. (NNNN.0)",
                        null=True,
                        verbose_name="Sequence",
                    ),
                ),
                (
                    "appt_datetime",
                    models.DateTimeField(
                        db_index=True, verbose_name="Appointment date and time"
                    ),
                ),
                (
                    "appt_type",
                    models.CharField(
                        choices=[
                            ("clinic", "In clinic"),
                            ("telephone", "By telephone"),
                            ("home", "At home"),
                        ],
                        default="clinic",
                        help_text="Default for subject may be edited Subject Configuration.",
                        max_length=20,
                        verbose_name="Appointment type",
                    ),
                ),
                (
                    "appt_status",
                    models.CharField(
                        choices=[
                            ("new", "New"),
                            ("in_progress", "In Progress"),
                            ("incomplete", "Incomplete"),
                            ("done", "Done"),
                            ("cancelled", "Cancelled"),
                        ],
                        db_index=True,
                        default="new",
                        max_length=25,
                        verbose_name="Status",
                    ),
                ),
                (
                    "appt_reason",
                    models.CharField(
                        blank=True,
                        help_text="Reason for appointment",
                        max_length=25,
                        verbose_name="Reason for appointment",
                    ),
                ),
                (
                    "comment",
                    models.CharField(blank=True, max_length=250, verbose_name="Comment"),
                ),
                ("is_confirmed", models.BooleanField(default=False, editable=False)),
                (
                    "consent_version",
                    models.CharField(default="?", editable=False, max_length=10),
                ),
            ],
            options={"abstract": False, "ordering": ("appt_datetime",)},
        ),
        migrations.CreateModel(
            name="HistoricalAppointment",
            fields=[
                (
                    "created",
                    django_extensions.db.fields.CreationDateTimeField(
                        auto_now_add=True, verbose_name="created"
                    ),
                ),
                (
                    "modified",
                    django_extensions.db.fields.ModificationDateTimeField(
                        auto_now=True, verbose_name="modified"
                    ),
                ),
                (
                    "user_created",
                    edc_model_fields.fields.userfield.UserField(
                        blank=True,
                        editable=False,
                        max_length=50,
                        verbose_name="user created",
                    ),
                ),
                (
                    "user_modified",
                    edc_model_fields.fields.userfield.UserField(
                        blank=True,
                        editable=False,
                        max_length=50,
                        verbose_name="user modified",
                    ),
                ),
                (
                    "hostname_created",
                    models.CharField(
                        default="mac2-2.local",
                        editable=False,
                        help_text="System field. (modified on create only)",
                        max_length=50,
                    ),
                ),
                (
                    "hostname_modified",
                    edc_model_fields.fields.hostname_modification_field.HostnameModificationField(
                        blank=True,
                        editable=False,
                        help_text="System field. (modified on every save)",
                        max_length=50,
                    ),
                ),
                (
                    "revision",
                    django_revision.revision_field.RevisionField(
                        blank=True,
                        editable=False,
                        help_text="System field. Git repository tag:branch:commit.",
                        max_length=75,
                        null=True,
                        verbose_name="Revision",
                    ),
                ),
                (
                    "id",
                    django_audit_fields.fields.uuid_auto_field.UUIDAutoField(
                        blank=True,
                        db_index=True,
                        editable=False,
                        help_text="System auto field. UUID primary key.",
                    ),
                ),
                (
                    "subject_identifier",
                    models.CharField(
                        editable=False, max_length=50, verbose_name="Subject Identifier"
                    ),
                ),
                (
                    "timepoint_status",
                    models.CharField(
                        choices=[
                            ("open", "Open"),
                            ("feedback", "Feedback"),
                            ("closed", "Closed"),
                        ],
                        default="open",
                        max_length=15,
                    ),
                ),
                (
                    "timepoint_opened_datetime",
                    models.DateTimeField(
                        editable=False,
                        help_text="the original calculated model's datetime, updated in the signal",
                        null=True,
                    ),
                ),
                (
                    "timepoint_closed_datetime",
                    models.DateTimeField(editable=False, null=True),
                ),
                (
                    "visit_schedule_name",
                    models.CharField(
                        editable=False,
                        help_text='the name of the visit schedule used to find the "schedule"',
                        max_length=25,
                    ),
                ),
                ("schedule_name", models.CharField(editable=False, max_length=25)),
                (
                    "visit_code",
                    models.CharField(editable=False, max_length=25, null=True),
                ),
                (
                    "timepoint",
                    models.DecimalField(
                        decimal_places=1,
                        editable=False,
                        help_text="timepoint from schedule",
                        max_digits=6,
                        null=True,
                    ),
                ),
                (
                    "timepoint_datetime",
                    models.DateTimeField(
                        editable=False,
                        help_text="Unadjusted datetime calculated from visit schedule",
                        null=True,
                    ),
                ),
                (
                    "appt_close_datetime",
                    models.DateTimeField(
                        editable=False,
                        help_text="timepoint_datetime adjusted according to the nearest available datetime for this facility",
                        null=True,
                    ),
                ),
                ("facility_name", models.CharField(max_length=25)),
                (
                    "visit_instance",
                    models.CharField(
                        blank=True,
                        db_index=True,
                        default="0",
                        help_text="A decimal to represent an additional report to be included with the original visit report. (NNNN.0)",
                        max_length=1,
                        null=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                "[0-9]", "Must be a number from 0-9"
                            )
                        ],
                        verbose_name="Instance",
                    ),
                ),
                (
                    "visit_code_sequence",
                    models.IntegerField(
                        blank=True,
                        default=0,
                        help_text="An integer to represent the sequence of additional appointments relative to the base appointment, 0, needed to complete data collection for the timepoint. (NNNN.0)",
                        null=True,
                        verbose_name="Sequence",
                    ),
                ),
                (
                    "appt_datetime",
                    models.DateTimeField(
                        db_index=True, verbose_name="Appointment date and time"
                    ),
                ),
                (
                    "appt_type",
                    models.CharField(
                        choices=[
                            ("clinic", "In clinic"),
                            ("telephone", "By telephone"),
                            ("home", "At home"),
                        ],
                        default="clinic",
                        help_text="Default for subject may be edited Subject Configuration.",
                        max_length=20,
                        verbose_name="Appointment type",
                    ),
                ),
                (
                    "appt_status",
                    models.CharField(
                        choices=[
                            ("new", "New"),
                            ("in_progress", "In Progress"),
                            ("incomplete", "Incomplete"),
                            ("done", "Done"),
                            ("cancelled", "Cancelled"),
                        ],
                        db_index=True,
                        default="new",
                        max_length=25,
                        verbose_name="Status",
                    ),
                ),
                (
                    "appt_reason",
                    models.CharField(
                        blank=True,
                        help_text="Reason for appointment",
                        max_length=25,
                        verbose_name="Reason for appointment",
                    ),
                ),
                (
                    "comment",
                    models.CharField(blank=True, max_length=250, verbose_name="Comment"),
                ),
                ("is_confirmed", models.BooleanField(default=False, editable=False)),
                (
                    "consent_version",
                    models.CharField(default="?", editable=False, max_length=10),
                ),
                ("history_date", models.DateTimeField()),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "history_id",
                    django_audit_fields.fields.uuid_auto_field.UUIDAutoField(
                        primary_key=True, serialize=False
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "get_latest_by": "history_date",
                "verbose_name": "historical appointment",
                "ordering": ("-history_date", "-history_id"),
            },
        ),
        migrations.AlterUniqueTogether(
            name="appointment",
            unique_together=set(
                [
                    (
                        "subject_identifier",
                        "visit_schedule_name",
                        "schedule_name",
                        "visit_code",
                        "visit_code_sequence",
                    ),
                    (
                        "subject_identifier",
                        "visit_schedule_name",
                        "schedule_name",
                        "visit_code",
                        "timepoint",
                    ),
                ]
            ),
        ),
    ]
