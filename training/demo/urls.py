from . import views
from django.urls import path
urlpatterns = [
    path('demo_plain/', views.demo_view, name='demo_plain'),
    path('demo_http/', views.demo_http, name='demo_http'),
    path('demo_http_template/', views.demo_http_template, name='demo_http_template'),
]