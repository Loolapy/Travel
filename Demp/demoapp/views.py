from django.shortcuts import render
from . models import team
# Create your views here.

from django.http import HttpResponse

def index(request):
    tm=team.objects.all
    return render(request,"index.html",{'resul':tm})
