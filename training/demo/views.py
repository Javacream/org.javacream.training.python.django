from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.template import loader
# Create your views here.

def demo_view(request: HttpRequest):
    result = HttpResponse('demo_view is working!')
    return result

def demo_http(request):
    return HttpResponse('<h1>Hello</h1><h2>World</h2>')

def demo_http_template(request):
    simple_page = loader.get_template('simple.html')
    return HttpResponse(simple_page.render())