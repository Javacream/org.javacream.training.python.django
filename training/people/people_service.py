import requests
from .global_links import global_links
from .models import Person
user = requests.get('http://javacream.eu:8080/people/6').json()
def get_context():    
    context = {'links': global_links, 'user': user, 'app_name': 'P E O P L E', 'company': 'Javacream'}
    return context

def get_context_for_people_list():    
    context = {'links': global_links, 'people': Person.objects.all(), 'user': user, 'app_name': 'P E O P L E', 'company': 'Javacream'}
    return context

def get_context_for_person(id):    
    context = {'links': global_links, 'person': Person.objects.get(pk=id), 'user': user, 'app_name': 'P E O P L E', 'company': 'Javacream'}
    return context
def create_person(lastname, firstname):
    Person.objects.create(lastname=lastname, firstname=firstname, height=176, weight=71.3)