from . import views
from django.urls import path
urlpatterns = [
    path('people/', views.people, name='people'),
    path('people/<str:page>/', views.people, name='people'),
    path('addresses/list/', views.ListView.as_view(), name='address_list'),
    path('addresses/new/', views.CreateView.as_view(), name='address_new'),
]