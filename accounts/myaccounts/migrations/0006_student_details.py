# Generated by Django 2.2 on 2019-06-14 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myaccounts', '0005_amount_details_remark'),
    ]

    operations = [
        migrations.CreateModel(
            name='student_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amt_date', models.DateTimeField(max_length=50)),
                ('session', models.CharField(max_length=30)),
                ('cour_year', models.CharField(max_length=20)),
                ('reg_no', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('father_name', models.CharField(max_length=100)),
                ('agent_name', models.CharField(max_length=100)),
                ('course', models.CharField(max_length=250)),
                ('amt_type', models.CharField(max_length=30)),
                ('amount', models.FloatField()),
                ('commission', models.FloatField()),
                ('mobile', models.CharField(max_length=10)),
                ('org_name', models.CharField(max_length=200)),
            ],
        ),
    ]
