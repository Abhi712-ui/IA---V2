from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def TaskList(request):
     return HttpResponse('To Do List')
