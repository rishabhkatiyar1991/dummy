# Generated by Django 2.2 on 2019-07-18 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dpsgsale', '0005_auto_20190717_0107'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product_details',
            old_name='images',
            new_name='pro_images',
        ),
    ]
