from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def demo_view(request):
    return HttpResponse('demo_view is working')