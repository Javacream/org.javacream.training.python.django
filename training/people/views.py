from django.shortcuts import render
from .people_service import get_context_for_people_list, get_context_for_person, get_context
from django.http import HttpRequest
from .forms import PersonInputForm

# Create your views here.

def people(request: HttpRequest, page=''):
    id = request.GET.get('id')
    if id:
        context = get_context_for_person(id)
        context['page'] = 'person'
    else:
        context = get_context()
        if page == 'peopleList':
            context = get_context_for_people_list()
            context['page'] = 'list'
        elif page == 'personInput':
            if request.method == "POST":
                form = PersonInputForm(request.POST)
                if form.is_valid():
                    first_name = form.cleaned_data["first_name"]
                    last_name = form.cleaned_data["last_name"]
                    print(first_name, last_name)

            else:
                form = PersonInputForm()
            context['page'] = 'person_input'
            context['form'] = form
    return render(request, 'people.html', context)


