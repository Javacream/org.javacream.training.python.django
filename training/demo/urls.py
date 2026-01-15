from . import views
from django.urls import path
urlpatterns = [
    path('demo/', views.demo_http_template, name='demo_http_template'),
    path('demo/params/', views.request_params, name='params'),
    path("demo/form/", views.simple_form, name="name_form"),
    path('demo/pathparam/<int:id>/', views.path_params, name='pathparam'),
]