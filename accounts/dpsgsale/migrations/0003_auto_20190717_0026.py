# Generated by Django 2.2 on 2019-07-16 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpsgsale', '0002_auto_20190717_0025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_details',
            name='flag',
            field=models.IntegerField(blank=True, default='0'),
        ),
    ]
