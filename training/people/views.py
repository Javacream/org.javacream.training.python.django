from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
# Create your views here.

def people(request):
    return HttpResponse(loader.get_template('people.html').render())