from django.db import models
from datetime import date
import os
# Create your models here.
class Course(models.Model):
    courseid = models.CharField(max_length=15, primary_key=True)
    coursename = models.CharField(max_length=40)
    id = models.ForeignKey('home.Examiner',  on_delete=models.CASCADE)
    #examinerid = models.CharField(max_length=50,default='02')

class Exam(models.Model):
    examid = models.CharField(max_length=40,  primary_key=True)
    examname = models.CharField(max_length=40)
    examdate = models.DateField(auto_now=False)
    courseid = models.ForeignKey('eadmin.Course', on_delete=models.CASCADE)
    examinerid = models.CharField(max_length=40, default='02')
    #tot_q = models.IntegerField


def content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s_%s.%s" % (instance.roll_no, 'paymentslip', ext)
    return os.path.join('documents/payment/', filename)



class Enrollments(models.Model):
    roll_no = models.ForeignKey('home.Applicant',  on_delete=models.CASCADE)
    examid = models.ForeignKey('eadmin.Exam',  on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    paymentref = models.FileField(upload_to=content_file_name)


    class Meta:
        unique_together = (("roll_no", "examid"),)



