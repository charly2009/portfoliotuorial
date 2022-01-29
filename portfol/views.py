from django.shortcuts import render, HttpResponse
from .models import Project

# Create your views here.

def home(request):
    project = Project.objects.all()
    return render(request, 'portfol/home.html', {'projects': project})
