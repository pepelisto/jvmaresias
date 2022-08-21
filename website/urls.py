from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


app_name = 'website'
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('test/', views.test, name='test'),
]
