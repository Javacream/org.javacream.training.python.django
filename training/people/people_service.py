import requests
context = {'user': requests.get('http://javacream.eu:8080/people/6').json(), 'app_name': 'P E O P L E', 'company': 'Javacream'}
