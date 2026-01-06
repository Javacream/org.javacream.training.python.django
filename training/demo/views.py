from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def demo_view(request):
    return HttpResponse('demo_view is working')
def demo_html(request):
    simple_page = loader.get_template('simple.html')
    return HttpResponse(simple_page.render())