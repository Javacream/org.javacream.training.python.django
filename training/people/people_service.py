import requests
from .global_links import global_links
context = {'links': global_links, 'people': requests.get('http://javacream.eu:8080/people').json(), 'user': requests.get('http://javacream.eu:8080/people/6').json(), 'app_name': 'P E O P L E', 'company': 'Javacream'}
