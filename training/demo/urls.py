from . import views
from django.urls import path
urlpatterns = [
    path('demo/', views.demo_view, name='demo'),
]