from django.shortcuts import render
from django.http import HttpResponse
from .models import Curriculum
def index1(request):
    return HttpResponse('index1')

def main(request):
    return HttpResponse('main!')   

def show(request):
    curriculum = Curriculum.objects.all()
    html = ''
    for c in curriculum:
        html += '%s번 %s<br>' % (c.id, c.name)
    return HttpResponse(html) 
# Create your views here.
