from unicodedata import name
from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('inside/', views.inside, name='berhasil'),
    path('register/', views.register, name='register'),
    path('register/process/', views.submitRegister, name='submitRegister')
]