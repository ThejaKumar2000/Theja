from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def theja(request):
    return HttpResponse('<marquee><h1>Theja is a student</h1></marquee>')