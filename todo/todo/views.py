from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.models import User

#import from apps=================

#views==================
class HomeView(LoginRequiredMixin,TemplateView):
    login_url='login'
    template_name="home.html"

def gotologin(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse_lazy("home"))
    else:
        return HttpResponseRedirect(reverse_lazy("login"))

def register_view(request):
    template_name = "register.html"

    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("pass")
        newuser = User.objects.create_user(
        username=username,
        password=password ,
        email=email
        )
        return HttpResponseRedirect(reverse_lazy("goto"))

    return render(request , template_name )

def login_view(request):
    template_name = "login.html"
    context = {'error':False}
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse_lazy("home"))
    else:
        if request.method == "POST":
            username=request.POST.get("username")
            password = request.POST.get("pass")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse_lazy("home"))
            else :
                context['error']=True
        return render(request , template_name , context=context)

@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy("login"))
