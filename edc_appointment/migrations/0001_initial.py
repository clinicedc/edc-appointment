# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-04 20:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_crypto_fields.fields.encrypted_text_field
import django_extensions.db.fields
import django_revision.revision_field
import edc_base.model.fields.hostname_modification_field
import edc_base.model.fields.userfield
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalTimePointStatus',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('user_created', edc_base.model.fields.userfield.UserField(editable=False, max_length=50, verbose_name='user created')),
                ('user_modified', edc_base.model.fields.userfield.UserField(editable=False, max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(default='mac2-2.local', editable=False, help_text='System field. (modified on create only)', max_length=50)),
                ('hostname_modified', edc_base.model.fields.hostname_modification_field.HostnameModificationField(editable=False, help_text='System field. (modified on every save)', max_length=50)),
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('id', models.UUIDField(blank=True, db_index=True, default=uuid.uuid4, editable=False, help_text='System auto field. UUID primary key.')),
                ('visit_code', models.CharField(max_length=15)),
                ('subject_identifier', models.CharField(max_length=25)),
                ('close_datetime', models.DateTimeField(blank=True, null=True, verbose_name='Date closed.')),
                ('status', models.CharField(choices=[('open', 'Open'), ('feedback', 'Feedback'), ('closed', 'Closed')], default='open', max_length=15)),
                ('comment', django_crypto_fields.fields.encrypted_text_field.EncryptedTextField(blank=True, help_text=' (Encryption: AES local)', max_length=500, null=True)),
                ('subject_withdrew', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], default='N/A', help_text='Use ONLY when subject has changed mind and wishes to withdraw consent', max_length=15, null=True, verbose_name='Did the participant withdraw consent?')),
                ('reasons_withdrawn', models.CharField(choices=[('changed_mind', 'Subject changed mind'), ('N/A', 'Not applicable')], default='N/A', max_length=35, null=True, verbose_name='Reason participant withdrew consent')),
                ('withdraw_datetime', models.DateTimeField(blank=True, null=True, verbose_name='Date and time participant withdrew consent')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'get_latest_by': 'history_date',
                'verbose_name': 'historical Time Point Completion',
                'ordering': ('-history_date', '-history_id'),
            },
        ),
        migrations.CreateModel(
            name='Holiday',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('user_created', edc_base.model.fields.userfield.UserField(editable=False, max_length=50, verbose_name='user created')),
                ('user_modified', edc_base.model.fields.userfield.UserField(editable=False, max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(default='mac2-2.local', editable=False, help_text='System field. (modified on create only)', max_length=50)),
                ('hostname_modified', edc_base.model.fields.hostname_modification_field.HostnameModificationField(editable=False, help_text='System field. (modified on every save)', max_length=50)),
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, help_text='System auto field. UUID primary key.', primary_key=True, serialize=False)),
                ('holiday_name', models.CharField(default='holiday', max_length=25)),
                ('holiday_date', models.DateField(unique=True)),
            ],
            options={
                'ordering': ['holiday_date'],
            },
        ),
        migrations.CreateModel(
            name='TimePointStatus',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('user_created', edc_base.model.fields.userfield.UserField(editable=False, max_length=50, verbose_name='user created')),
                ('user_modified', edc_base.model.fields.userfield.UserField(editable=False, max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(default='mac2-2.local', editable=False, help_text='System field. (modified on create only)', max_length=50)),
                ('hostname_modified', edc_base.model.fields.hostname_modification_field.HostnameModificationField(editable=False, help_text='System field. (modified on every save)', max_length=50)),
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, help_text='System auto field. UUID primary key.', primary_key=True, serialize=False)),
                ('visit_code', models.CharField(max_length=15)),
                ('subject_identifier', models.CharField(max_length=25)),
                ('close_datetime', models.DateTimeField(blank=True, null=True, verbose_name='Date closed.')),
                ('status', models.CharField(choices=[('open', 'Open'), ('feedback', 'Feedback'), ('closed', 'Closed')], default='open', max_length=15)),
                ('comment', django_crypto_fields.fields.encrypted_text_field.EncryptedTextField(blank=True, help_text=' (Encryption: AES local)', max_length=500, null=True)),
                ('subject_withdrew', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], default='N/A', help_text='Use ONLY when subject has changed mind and wishes to withdraw consent', max_length=15, null=True, verbose_name='Did the participant withdraw consent?')),
                ('reasons_withdrawn', models.CharField(choices=[('changed_mind', 'Subject changed mind'), ('N/A', 'Not applicable')], default='N/A', max_length=35, null=True, verbose_name='Reason participant withdrew consent')),
                ('withdraw_datetime', models.DateTimeField(blank=True, null=True, verbose_name='Date and time participant withdrew consent')),
            ],
            options={
                'verbose_name_plural': 'Time Point Completion',
                'verbose_name': 'Time Point Completion',
                'ordering': ['subject_identifier', 'visit_code'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='timepointstatus',
            unique_together=set([('subject_identifier', 'visit_code')]),
        ),
    ]