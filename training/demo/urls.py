from django.urls import path
from . import views

urlpatterns = [
    path('demo/simple/', views.demo_view, name='demo_simple'),
    path('demo/html/', views.demo_html, name='demo_html'),
]
