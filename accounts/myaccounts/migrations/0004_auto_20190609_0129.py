# Generated by Django 2.2 on 2019-06-08 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myaccounts', '0003_auto_20190609_0104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amount_details',
            name='amt_date',
            field=models.CharField(max_length=50),
        ),
    ]
