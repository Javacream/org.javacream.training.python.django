from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.template import loader
from people.global_links import global_links
# Create your views here.

def demo_http_template(request):
    return render(request, 'simple.html', {'links': global_links}) 
def params(request: HttpRequest):
    context = {
        'name': request.GET.get('username')
    }
    return render(request, 'params.html', context)
