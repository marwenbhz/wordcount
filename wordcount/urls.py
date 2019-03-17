from django.urls import path

from . import views

urlpatterns = [
    path('', views.wordcount, name='wordcount'),
]
