from . import views
from django.urls import path
urlpatterns = [
    path('people/', views.people, name='people'),
]