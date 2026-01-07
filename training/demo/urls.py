from . import views
from django.urls import path
urlpatterns = [
    path('demo/', views.demo_http_template, name='demo_http_template'),
]