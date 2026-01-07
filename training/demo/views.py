from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.template import loader
# Create your views here.

def demo_http_template(request):
    simple_page = loader.get_template('simple.html')
    return HttpResponse(simple_page.render())