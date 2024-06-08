from django.urls import path

from web import views

urlpatterns = [
    path('', views.inicio,name='inicio'),
]
