from django.urls import path
from . import views

urlpatterns = [
    path('', views.form, name='form'),
    path('data/', views.data, name='data'),
    #path('form/', views.form, name='form')
]
