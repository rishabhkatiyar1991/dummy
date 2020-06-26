from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class amount_details(models.Model):
    amt_date = models.CharField(max_length=50)
    user_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    org_name = models.CharField(max_length=100)
    amt_type = models.CharField(max_length=20)
    amount = models.FloatField()
    mobile = models.CharField(max_length=10)
    remark = models.CharField(max_length=255, blank=True)

class student_details(models.Model):
    amt_date = models.DateTimeField(max_length=50)
    session_time = models.CharField(max_length=30)
    cour_year = models.CharField(max_length=20)
    reg_no = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=100)
    agent_name = models.CharField(max_length=100)
    course = models.CharField(max_length=250)
    amt_type = models.CharField(max_length=30)
    amount = models.FloatField(default='0')
    fee = models.FloatField(default='0')
    commission = models.FloatField(default='0')
    mobile = models.CharField(max_length=10)
    org_name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.first_name

    def __str__(self):
        return self.first_name



