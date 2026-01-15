import requests
from .global_links import global_links

def get_context():    
    context = {'links': global_links, 'user': requests.get('http://javacream.eu:8080/people/6').json(), 'app_name': 'P E O P L E', 'company': 'Javacream'}
    return context

def get_context_for_people_list():    
    context = {'links': global_links, 'people': requests.get('http://javacream.eu:8080/people').json(), 'user': requests.get('http://javacream.eu:8080/people/6').json(), 'app_name': 'P E O P L E', 'company': 'Javacream'}
    return context

def get_context_for_person(id):    
    context = {'links': global_links, 'person': requests.get(f'http://javacream.eu:8080/people/{id}').json(), 'user': requests.get('http://javacream.eu:8080/people/6').json(), 'app_name': 'P E O P L E', 'company': 'Javacream'}
    return context
