from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
import datetime

#import from apps==========
from .models import JobsModel

# Create your views here.=========
def find_job(user , kind , done , working , today=None):
    if not today:
        jobs = JobsModel.objects.today().filter(owner= user
        ).filter(kind=kind
        ).filter(done=done
        ).filter(working=working)
    else :
        jobs = JobsModel.objects.all().filter(date=today
        ).filter(owner= user
        ).filter(kind=kind
        ).filter(done=done
        ).filter(working=working)
    return jobs

@login_required(login_url='login')
def my_personal_list(request):
    template_name="myjobspersonal.html"
    context={'error':False , 'dateerror': False}
    changedate=request.GET.get("date")
    todo = find_job(user= request.user , kind='p' , done = False , working=False )
    working = find_job(user= request.user , kind='p' , done = False , working=True)
    done = find_job(user= request.user , kind='p' , done = True , working=False)
#==============================
    if changedate:
        todo = find_job(user= request.user , kind='p' , done = False , working=False ,today=changedate )
        working = find_job(user= request.user , kind='p' , done = False , working=True ,today=changedate)
        done = find_job(user= request.user , kind='p' , done = True , working=False ,today=changedate)
    context['todo']=todo
    context['working']=working
    context['done']=done
    today = datetime.date.today()
    compareday = str(datetime.date.today())
    compareday = compareday.replace("-","")
    compareday=int(compareday)
    if request.method == "POST":
        newjob = request.POST.get("newjobtext")
        datenew = request.POST.get("datenew")
        if datenew:
            comparedatenew = datenew.replace("-","")
            comparedatenew = int(comparedatenew)
        if newjob :
            if datenew :
                if comparedatenew < compareday :
                    context['dateerror']=True
                else:
                    today=datenew
            if not context['dateerror'] :
                JobsModel.objects.create(
                owner = request.user,
                kind = "p",
                content = newjob,
                date = today
                )
                return HttpResponseRedirect(reverse_lazy("personal:base"))
        else :
            context['error']=True
    return render(request , template_name , context)

def next_step(request , *args , **kwargs):
    slug = kwargs['slug']
    job = JobsModel.objects.get(slug = slug)
    if job.working :
        job.working=False
        job.done=True
        job.save()
    else:
        job.working = True
        job.save()
    return HttpResponseRedirect(reverse_lazy("personal:base"))
