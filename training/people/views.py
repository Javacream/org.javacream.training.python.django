from django.shortcuts import render
from .people_service import get_context_for_people_list, get_context_for_person
# Create your views here.

def people(request):
    id = request.GET.get('id')
    if id:
        context = get_context_for_person(id)
        context['page'] = 'person'
    else:
        context = get_context_for_people_list()
        context['page'] = 'list'
    return render(request, 'people.html', context)

