from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.

def demo_view(request: HttpRequest):
    result = HttpResponse('demo_view is working!')
    return result