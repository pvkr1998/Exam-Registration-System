from django.db import models

# Create your models here.

class Applicant(models.Model):
    roll_no = models.CharField(max_length=15, primary_key=True)
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=500)
    email = models.CharField(max_length=30)
    mobile_no = models.CharField(max_length=13)
    last_login = models.DateTimeField


class Examiner(models.Model):
    id = models.CharField(max_length=15, primary_key=True)
    password = models.CharField(max_length=500)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)


class Admin(models.Model):
    id = models.CharField(max_length=15, primary_key=True)
    password = models.CharField(max_length=500)
    email = models.CharField(max_length=50)


