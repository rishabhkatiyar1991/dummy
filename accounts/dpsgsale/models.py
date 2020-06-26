from django.db import models
from django.contrib.auth.models import User
#from passlib.hash import pbkdf2_sha256
#from django.contrib.auth.hashers import check_password


# Create your models here.


class product_details(models.Model):
    pro_date = models.DateTimeField(max_length=50)
    user_id = models.IntegerField(default='0')
    username = models.CharField(max_length=20)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    class_name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)
    price = models.FloatField(default='0')
    flag = models.IntegerField(default='0', blank=True)
    pro_images = models.ImageField(upload_to='images/')
    purch_userid = models.IntegerField(default='0', null=True)
    purch_username = models.CharField(max_length=20, null=True)
    purch_first_name = models.CharField(max_length=50, null=True)
    purch_last_name = models.CharField(max_length=50, null=True)
    purch_date = models.DateTimeField(max_length=50, null=True)


    def __unicode__(self):
        return self.first_name

    def __str__(self):
        return self.first_name+":"+str(self.pro_images)




