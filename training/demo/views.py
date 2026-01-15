from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.template import loader
from people.global_links import global_links
from .forms import NameForm
# Create your views here.

def demo_http_template(request):
    return render(request, 'simple.html', {'links': global_links}) 
def params(request: HttpRequest):
    context = {
        'name': request.GET.get('username')
    }
    return render(request, 'params.html', context)



def simple_form(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            print(first_name, last_name)

    else:
        form = NameForm()

    return render(request, "name_form.html", {"form": form})
