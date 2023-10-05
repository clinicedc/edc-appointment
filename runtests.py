#!/usr/bin/env python
import logging
import os
import sys
from datetime import datetime
from os.path import abspath, dirname
from zoneinfo import ZoneInfo

import django
from django.conf import settings
from django.test.runner import DiscoverRunner
from edc_test_utils import DefaultTestSettings

utc = ZoneInfo("UTC")

app_name = "edc_appointment"
base_dir = dirname(abspath(__file__))

DEFAULT_SETTINGS = DefaultTestSettings(
    calling_file=__file__,
    BASE_DIR=base_dir,
    APP_NAME=app_name,
    ETC_DIR=os.path.join(base_dir, app_name, "tests", "etc"),
    EDC_NAVBAR_AUTODISCOVER=False,
    EDC_PROTOCOL_STUDY_OPEN_DATETIME=datetime(2016, 10, 2, 0, 0, 0, tzinfo=utc),
    EDC_PROTOCOL_STUDY_CLOSE_DATETIME=datetime(2023, 10, 2, 0, 0, 0, tzinfo=utc),
    EDC_AUTH_SKIP_SITE_AUTHS=True,
    EDC_AUTH_SKIP_AUTH_UPDATER=True,
    SUBJECT_SCREENING_MODEL="edc_appointment_app.subjectscreening",
    SUBJECT_CONSENT_MODEL="edc_appointment_app.subjectconsent",
    SUBJECT_VISIT_MODEL="edc_appointment_app.subjectvisit",
    SUBJECT_VISIT_MISSED_MODEL="edc_appointment_app.subjectvisitmissed",
    SUBJECT_REQUISITION_MODEL="edc_appointment_app.subjectrequisition",
    SUBJECT_APP_LABEL="edc_appointment_app",
    INSTALLED_APPS=[
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        "django.contrib.sites",
        "django_crypto_fields.apps.AppConfig",
        "django_revision.apps.AppConfig",
        "multisite",
        "edc_auth.apps.AppConfig",
        "edc_action_item.apps.AppConfig",
        "edc_offstudy.apps.AppConfig",
        "edc_consent.apps.AppConfig",
        "edc_crf.apps.AppConfig",
        "edc_dashboard.apps.AppConfig",
        "edc_data_manager.apps.AppConfig",
        "edc_lab.apps.AppConfig",
        "edc_subject_dashboard.apps.AppConfig",
        "edc_device.apps.AppConfig",
        "edc_facility.apps.AppConfig",
        "edc_identifier.apps.AppConfig",
        "edc_list_data.apps.AppConfig",
        "edc_listboard.apps.AppConfig",
        "edc_locator.apps.AppConfig",
        "edc_metadata.apps.AppConfig",
        "edc_model_admin.apps.AppConfig",
        "edc_navbar.apps.AppConfig",
        "edc_protocol.apps.AppConfig",
        "edc_randomization.apps.AppConfig",
        "edc_reference.apps.AppConfig",
        "edc_registration.apps.AppConfig",
        "edc_notification.apps.AppConfig",
        "edc_review_dashboard.apps.AppConfig",
        "edc_sites.apps.AppConfig",
        "edc_timepoint.apps.AppConfig",
        "edc_visit_schedule.apps.AppConfig",
        "edc_visit_tracking.apps.AppConfig",
        "edc_appointment.apps.AppConfig",
        "edc_appointment_app.apps.AppConfig",
    ],
    add_dashboard_middleware=True,
    use_test_urls=True,
).settings


def main():
    if not settings.configured:
        settings.configure(**DEFAULT_SETTINGS)
    django.setup()
    tags = [t.split("=")[1] for t in sys.argv if t.startswith("--tag")]
    failfast = True if [t for t in sys.argv if t == "--failfast"] else False
    failures = DiscoverRunner(failfast=failfast, tags=tags).run_tests([f"{app_name}.tests"])
    sys.exit(failures)


if __name__ == "__main__":
    logging.basicConfig()
    main()
