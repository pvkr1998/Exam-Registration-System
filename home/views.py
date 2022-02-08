from django.shortcuts import render, redirect
from django import forms
from home.models import Examiner, Admin, Applicant
from .forms import RegForm, LoginForm
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import login


from django.views import generic


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            userdet = form.cleaned_data
            rollno = userdet['rollno']
            password = userdet['password']

            val = request.POST.getlist('user')

            errflag = 0
            user = None

            if val[0] == 'c1':
                if not Applicant.objects.filter(roll_no=rollno).exists():
                    errflag = 1
                else:
                    user = Applicant.objects.get(roll_no=rollno)
            if val[0] == 'c2':
                if not Examiner.objects.filter(id=rollno).exists():
                    errflag = 1
                else:
                    user = Examiner.objects.get(id=rollno)
            elif val[0] == 'c3':
                if not Admin.objects.filter(id=rollno).exists():
                    errflag = 1
                else:
                    user = Admin.objects.get(id=rollno)

            if errflag == 1:
                return render(request, 'home/index.html', {'msg': 'Please enter valid UserId'})
            else:
                if check_password(password, user.password):
                    if val[0] == 'c1':
                        request.session['id'] = user.roll_no
                        return redirect('/shome/')
                    elif val[0] == 'c2':
                        request.session['id'] = user.id
                        return redirect('/examiner/examhome/')
                        #return render(request, 'home/index.html', {'msg': 'c2 is selected'})
                    elif val[0] == 'c3':

                        #return render(request, 'home/index.html', {'msg': 'c3 is selected'})
                        request.session['id'] = user.id
                        return redirect('/adminhome/')
                    else:
                        return render(request, 'home/index.html', {'msg': 'Please choose login type'})
                else:
                    return render(request, 'home/index.html', {'msg': 'Enter a valid  Password'})
        else:
            return render(request, 'home/index.html', {'msg': 'Select all the required fields'})
    else:
        return render(request, 'home/index.html', None)


def register(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            userobj = form.cleaned_data
            username = userobj['username']
            roll_no = userobj['roll_no']
            email = userobj['email']
            password = userobj['password']
            rpassword = userobj['rpassword']
            phno = userobj['phno']

            flag = 0

            if Applicant.objects.filter(username=username).exists():
                errors = 'username already exists'
                flag = 1
            elif Applicant.objects.filter(roll_no=roll_no).exists():
                errors = 'Roll No already exists'
                flag = 1
            elif Applicant.objects.filter(email=email).exists():
                errors = 'EmailId already exists'
                flag = 1
            elif Applicant.objects.filter(mobile_no=phno).exists():
                errors = 'Phone No already exists'
                flag = 1
            elif password != rpassword:
                errors = 'Passwords do not match'
                flag = 1
            elif len(phno) < 10:
                errors = 'Please enter valid Phone No:'
                flag = 1

            if flag == 1:
                return render(request, 'home/registration.html', {'errors': errors})
            else:
                obj = Applicant(username=username, roll_no=roll_no, email=email, password=make_password(password),
                                mobile_no=phno)
                #Applicant.create(roll_no, username, password, email, phno)
                obj.save()
                msg = 'You have Successfully registered!'
                return render(request, 'home/registration.html', {'errors': msg})
        else:
            return render(request, 'home/registration.html', {'errors': 'Please enter valid details'})
    else:
        form = RegForm()
        return render(request, 'home/registration.html', {'form': form})



