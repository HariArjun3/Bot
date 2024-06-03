from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('get_resume/', views.get_resume, name='get_resume'),
]

