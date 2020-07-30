from django.shortcuts import render
from django.http import HttpResponse
from .models import hospital

def show(request):
    hos = hospital.objects.all()
    return render(request,"hospital.html",{'list' : hos})
def index1(request):
    return HttpResponse("ddfa")
# Create your views here.
