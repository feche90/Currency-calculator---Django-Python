from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('euro', views.euro, name='euro'),
    path('jpy', views.jpy, name='jpy'),
    path('cop', views.cop, name='cop'),
    path('usd', views.usd, name='usd'),
    path('result', views.result, name='result'),

]