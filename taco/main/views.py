from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
import os

def index(request):
  return render(request,"main/index.html")

def shutdown(request):
  os._exit(0)
  return render(request,"main/index.html")
