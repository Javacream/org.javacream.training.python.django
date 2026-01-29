from django.shortcuts import render
from .people_service import get_context_for_people_list, get_context_for_person, get_context, create_person
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
                    create_person(first_name, last_name)

            else:
                form = PersonInputForm()
            context['page'] = 'person_input'
            context['form'] = form
    return render(request, 'people.html', context)

from django.views.generic import CreateView, ListView
from .models import Address
class AddressCreateView(CreateView):
    model = Address
    fields = ['street', 'city']
    template_name = 'people/address_input.html'
class AddressListView(ListView):
    model = Address
    context_object_name = 'addresses'
    template_name = 'people/address_list.html'
