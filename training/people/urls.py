from . import views
from django.urls import path
urlpatterns = [
    path('people/', views.people, name='people'),
    path('people/<str:page>/', views.people, name='people'),
]