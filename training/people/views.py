from django.shortcuts import render
from .people_service import context
# Create your views here.

def people(request):
    return render(request, 'people.html', context)