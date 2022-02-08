from eadmin.models import Course, Enrollments, Exam
from home.models import Applicant,Admin,Examiner
from django.views.decorators.csrf import csrf_exempt
from pprint import pprint
from django.contrib.auth import logout as django_logout
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from datetime import date
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from datetime import datetime
from django.db.models import Q


def adminhome(request):
    enrollments = Enrollments.objects.filter(status='pending')
    return render(request, 'eadmin/adhome.html', {'objs': enrollments})

def addexam(request):
 #print('lala')
 if request.method == 'POST':
    CourseId = request.POST["CourseId"]
    ExamId = request.POST.get('ExamId', '')
    ExamName = request.POST.get('ExamName', '')
    #ExaminerId = request.POST.get('ExaminerId', '')
    Date = request.POST.get('Date', '')

    #print(CourseId+'hii'+ExamId)

    if len(CourseId) == 0 or len(ExamId) == 0 or len(Date) == 0:
        message = 'Please enter all the fields'
        print(message)
    elif not Course.objects.filter(courseid=CourseId).exists():
        message = 'course id doesnot exist'
    # elif not Examiner.objects.filter(id=ExaminerId).exists():
    #     message = 'Examiner id doesnot exist'
    elif Exam.objects.filter(examid=ExamId).exists():
        message = 'ExamId already exists'
    elif Exam.objects.filter(courseid=Course.objects.get(courseid=CourseId),examdate__gt=date.today()).exists():
        message = 'Exam already created'
    else:
        message = 'You have Successfully created!'
        obj= Course.objects.get(courseid=CourseId)
        x = Exam(examid= ExamId, examname=ExamName, examdate=Date, courseid=obj, examinerid=obj.id.id)
        x.save()

    return render(request, 'eadmin/adm_add_exam.html', {'message': message})
 else:
    #print('hello')
    return render(request, 'eadmin/adm_add_exam.html', None)


def addcourse(request):
 if request.method == 'POST':
    CourseId = request.POST.get('CourseId', '')
    CourseName = request.POST.get('CourseName', '')
    ExaminerId = request.POST.get('ExaminerId', '')
    message=''
    if len(CourseId) == 0 or len(CourseName) == 0 or len(ExaminerId) == 0:
        message = 'Please enter all the fields'
    elif Course.objects.filter(courseid=CourseId).exists():
        message = 'Course ID already exists'
    elif not Examiner.objects.filter(id=ExaminerId).exists():
        message = 'Examiner id doesnot exist'
    else:
        message = 'You have Successfully added a course!'
        obj = Examiner.objects.get(id=ExaminerId)
        x=Course(courseid = CourseId, coursename = CourseName,id = obj)
        x.save()
    return render(request,  'eadmin/addcourse.html', {'message': message})
 else:
    return render(request, 'eadmin/addcourse.html', None)



def adminprofile(request):
    rno = request.session['id']
    obj = Admin.objects.get(id=rno)
    if request.method == 'POST':
        email = request.POST["email"]

        if len(email) == 0:
            msg = 'Please enter all the fields'
        elif Admin.objects.filter(email=email).exists() and email != obj.email:
            msg = 'Email Id already exists'
        else:
            msg = 'Your profile has been sucessfully updated'
            obj.email = email
            obj.save()
        return render(request, 'eadmin/adminprofile.html', {'msg': msg, 'obj': obj})
    else:
        return render(request, 'eadmin/adminprofile.html', {'obj': obj})

@csrf_exempt
def adminchangepassword(request):
    if request.method == 'POST':
        oldpass = request.POST["opass"]
        npass = request.POST["npass"]
        rnpass = request.POST["rnpass"]
        Id = request.session['id']
        obj = Admin.objects.get(id=Id)
        epass = obj.password
        if len(npass) == 0 or len(oldpass) == 0 or len(rnpass) == 0:
            msg = 'Please enter all the fields'
        elif not check_password(oldpass, epass):
            msg = 'Please enter the existing password'
        elif npass != rnpass:
            msg = 'Passwords do not match'
        else:
            unpass = make_password(npass)
            msg = 'Your password has been updated'
            obj.password = unpass
            obj.save()
        return render(request, 'eadmin/adminchangepassword.html', {'msg': msg})
    else:
        return render(request, 'eadmin/adminchangepassword.html', None)



def alogout(request):
    return render(request, 'home/index.html', {'msg': 'You have sucessfully logged out!'})

def accept(request,p1,p2):
    obj=Enrollments.objects.get(roll_no=Applicant.objects.get(roll_no=p2),examid=Exam.objects.get(examid=p1))

   # print(parameter.status)
   # print(p1+p2)
    obj.status = 'verified'
    obj.save()
    enrollments = Enrollments.objects.filter(status='pending')
    return render(request, 'eadmin/adhome.html', {'objs': enrollments})

def reject(request,p1,p2):
    obj = Enrollments.objects.get(roll_no=Applicant.objects.get(roll_no=p2), examid=Exam.objects.get(examid=p1))
    #print(parameter)
    #parameter.status='rejected'
    #parameter.save()
    obj.status = 'rejected'
    obj.save()
    enrollments = Enrollments.objects.filter(status='pending')
    return render(request, 'eadmin/adhome.html', {'objs': enrollments})

