# Generated by Django 2.2 on 2019-06-14 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myaccounts', '0006_student_details'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student_details',
            old_name='session',
            new_name='session_time',
        ),
    ]
