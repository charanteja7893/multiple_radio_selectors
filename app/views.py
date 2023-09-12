from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse

def registration(request):
    ERFO=Registrationform()
    
    d={'ERFO':ERFO}

    if request.method=='POST':
        RF=Registrationform(request.POST)
        if RF.is_valid():
            return HttpResponse(str(RF.cleaned_data))
    return render(request,'registration.html',d)