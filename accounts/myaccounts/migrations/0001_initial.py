# Generated by Django 2.2 on 2019-06-07 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='amount_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=20)),
                ('user_name', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=50)),
                ('father_name', models.CharField(max_length=50)),
                ('org_name', models.CharField(max_length=100)),
                ('amt_type', models.CharField(max_length=20)),
                ('amount', models.FloatField()),
                ('mobile', models.IntegerField()),
            ],
        ),
    ]
