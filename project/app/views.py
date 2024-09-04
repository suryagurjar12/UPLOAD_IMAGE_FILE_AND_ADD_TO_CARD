from django.shortcuts import render
from .forms import *
from .models import *

# Create your views here.

def home(request):
    form= ItemInfoForm()
    if request.method=='POST':
        form = ItemInfoForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    
    return render(request,'home.html',{'form':form})


def showdata(request):
    data=ItemInfo.objects.all()
    data1 = data.values()
    return render(request,'dashboard.html',{'data':data1})
