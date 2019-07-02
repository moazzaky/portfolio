from django.shortcuts import render
from .models import Job

# Create your views here.

def home(request):
    jobs_list = Job.objects
    return  render(request, 'jobs\home.html', {'jobs_list':jobs_list})