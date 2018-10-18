from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy


from .models import GroupModel
# Create your views here.

def newgp_view(request):
    template_name="newgp.html"
    context={'exists' : False}
    if request.method == "POST":
        gpname = request.POST.get("name")
        check = GroupModel.objects.filter(name=gpname)
        if check:
            context['exists']= True
        else:
            creategp= GroupModel.objects.create(name=gpname)
            return HttpResponseRedirect(reverse_lazy("group:newgp"))
    if request.method == "GET":
        qname = request.GET.get("qname")
        query = GroupModel.objects.filter(name=qname)
        print(query)
    return render(request , template_name,context)
