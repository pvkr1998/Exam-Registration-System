from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from .forms import addexam, addquestion
from .models import  questions, Results, responses
from eadmin.models import Course, Enrollments, Exam
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth import logout as django_logout

from django.conf import settings
from django.core.files.storage import FileSystemStorage


# Create your views here.

@csrf_exempt
def addq(request):
    if request.method == 'POST':
        if request.POST.get('sub'):
            form = addquestion(request.POST)
            if form.is_valid():
                q = questions()
                q.examid = request.POST.get('examid')
                q.qid = request.POST.get('qid')
                q.q = request.POST.get('q')
                q.opta = request.POST.get('opta')
                q.optb = request.POST.get('optb')
                q.optc = request.POST.get('optc')
                q.optd = request.POST.get('optd')
                q.answer = request.POST.get('answer')
                try:
                    q.save()
                    return render(request, 'examhome.html', {'qs': 'Question Added'})
                except IntegrityError as ie:
                    return render(request, 'examhome.html',
                                  {'edit': 'yes', 'eerr': 'Choose a different id', 'examid': q.examid, 'qid': q.qid,
                                   'q': q.q, 'opta': q.opta, 'optb': q.optb, 'optc': q.optc, 'optd': q.optd,
                                   'answer': q.answer})
            else:
                return render(request, 'examhome.html', {'edit': 'yes', 'eerr': 'Enter all details correctly'})
        elif request.POST.get('edit'):
            print("yea")
            eqid = request.POST.get('eqid')
            count = questions.objects.filter(qid=eqid).count()
            if count == 0:
                return render(request, 'examhome.html', {'iderr': 'Question id invalid', 'qid': eqid})
            else:
                qe = questions.objects.get(qid=eqid)
                return render(request, 'examhome.html',
                              {'edt': 'yes', 'edit': 'yes', 'examid': qe.examid, 'qid': qe.qid, 'q': qe.q,
                               'opta': qe.opta, 'optb': qe.optb, 'optc': qe.optc, 'optd': qe.optd, 'answer': qe.answer})
        else:
            print("yea")
            form = addquestion(request.POST)
            q = questions()
            q.examid = request.POST.get('examid')
            q.qid = request.POST.get('qid')
            q.q = request.POST.get('q')
            q.opta = request.POST.get('opta')
            q.optb = request.POST.get('optb')
            q.optc = request.POST.get('optc')
            q.optd = request.POST.get('optd')
            q.answer = request.POST.get('answer')
            if form.is_valid():
                questions.objects.filter(examid=q.examid, qid=q.qid).update(q=q.q, opta=q.opta, optb=q.optb,
                                                                            optc=q.optc, optd=q.optd, answer=q.answer)
                return render(request, 'examhome.html', {'qs': 'Question updated'})
            else:
                return render(request, 'examhome.html',
                              {'edt': 'yes', 'edit': 'yes', 'eerr': 'Enter all details correctly', 'examid': q.examid,
                               'qid': q.qid, 'q': q.q, 'opta': q.opta, 'optb': q.optb, 'optc': q.optc, 'optd': q.optd,
                               'answer': q.answer})
    else:
        print("yea")
        template = loader.get_template('examhome.html')
        return HttpResponse(template.render())


@csrf_exempt

def logout(request):
    django_logout(request)
    #return redirect('/ExamReg/')
    return render(request,'home\index.html', {'msg': 'You have sucessfully logged out!'})

@csrf_exempt
def result(request):
    if request.method == 'POST':
        id = request.POST.get('id')

        print(id)
        res = Results.objects.filter(examid=Exam.objects.get(examid=id))

        # for item in res:
        #     print(item.roll_no.roll_no)

        return render(request, 'viewres.html', {'res': res})
        # template = loader.get_template('viewres.html')
        # return HttpResponse(template.render())
    else:
        # template = loader.get_template('viewres.html')
        # return HttpResponse(template.render())
        return render(request, 'viewres.html', None)


@csrf_exempt
def exam(request):
    if request.method == 'POST':
        qs = questions.objects.filter(examid=request.session["examid"])
        cor = 0
        wrg = 0
        tq = questions.objects.filter(examid=request.session["examid"]).count()
        j = 1
        sel = ""
        for i in qs:
            if (request.POST.get(str(j))):
                sel = sel + "," + str(request.POST.get(str(j)))
                if (request.POST.get(str(j)) == i.answer):
                    cor = cor + 1
                else:
                    wrg = wrg + 1
            else:
                sel = sel + ",none"
            j = j + 1
        un = tq - cor - wrg
        qs = responses()
        qs.examid = request.session["examid"]
        qs.studid = request.session["studid"]
        qs.reponse = sel
        qs.cor = cor
        qs.wrg = wrg
        qs.una = un
        qs.total = cor - wrg * 0.25
        qs.save()
        return HttpResponse("correct" + str(cor) + "wrong" + str(wrg) + "unattempted" + str(un))

    else:
        request.session["examid"] = "e1"
        request.session["studid"] = "1234"
        qs = questions.objects.filter(examid=request.session["examid"])
        template = loader.get_template('exam.html')
        return render(request, 'exam.html', {'q': qs})


@csrf_exempt
def exam(request):
    if request.method == 'POST':
        qs = questions.objects.filter(examid=request.session["examid"])
        cor = 0
        wrg = 0
        tq = questions.objects.filter(examid=request.session["examid"]).count()
        j = 1
        sel = ""
        for i in qs:
            if (request.POST.get(str(j))):
                sel = sel + "," + str(request.POST.get(str(j)))
                if (request.POST.get(str(j)) == i.answer):
                    cor = cor + 1
                else:
                    wrg = wrg + 1
            else:
                sel = sel + ",none"
            j = j + 1
        un = tq - cor - wrg
        qs = responses()
        qs.examid = request.session["examid"]
        qs.studid = request.session["id"]
        qs.reponse = sel
        qs.cor = cor
        qs.wrg = wrg
        qs.una = un
        qs.total = cor - wrg * 0.25
        qs.save()
        return HttpResponse("correct" + str(cor) + "wrong" + str(wrg) + "unattempted" + str(un))

    else:
        #request.session["examid"] = "e1"
        # request.session["id"] = "1234"
        qs = questions.objects.filter(examid=request.session["examid"])
        template = loader.get_template('exam.html')
        return render(request, 'exam.html', {'q': qs})


@csrf_exempt
def comp(request):

    if request.method == 'POST':
        qs = questions.objects.filter(examid=request.session["examid"])
        cor = 0
        wrg = 0
        tq = questions.objects.filter(examid=request.session["examid"]).count()
        j = 1
        sel = ""
        for i in qs:
            if(request.POST.get(str(j))):
                sel = sel + "," + str(request.POST.get(str(j)))
                if(request.POST.get(str(j)) == i.answer):
                    cor = cor+1
                else:
                    wrg = wrg+1
            else:
                sel = sel + ",none"
            j = j+1
        un=tq-cor-wrg
        qs = responses()
        qs.examid = request.session["examid"]
        qs.studid = request.session["id"]
        qs.reponse = sel
        qs.cor = cor
        qs.wrg = wrg
        qs.una = un
        qs.total = cor - wrg*0.25
        qs.save()
        at = cor + wrg
        total = cor - wrg*0.25
        return render(request,'displayresult.html',{'cor':cor,'wrg':wrg,'un':un,'total':total,'at':at})


