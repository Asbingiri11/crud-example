from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Detail
from .forms import *
# Create your views here.
def index(request):
    details= Detail.objects.all()
    form =DetailForm()
    context={
        'details': details
        

    }

    return render(request,'home.html',context)


def create(request):
    form = DetailForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
    context = {
        'form':form,
        'form_type':"Create"
    }
    return render(request,"create.html",context)

def details(request,pk):
    details = Detail.objects.get(id=pk)
    context = {
        'details' : details
    }
    return render(request,'details.html',context)

def update(request,pk):
    details = Detail.objects.get(id=pk)
    form = DetailForm(request.POST or None,instance=details)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
    context = {
        
        'form': form,
        'form_type':"update"
    }
    return render(request,"create.html",context)

def delete(request,pk):
    details = Detail.objects.get(id=pk)
    details.delete()
    return HttpResponseRedirect("/")
