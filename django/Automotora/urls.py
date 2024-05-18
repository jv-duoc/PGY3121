from django.urls import path

from Automotora import views

urlpatterns = [
    path('',views.inicio),
    path('info',views.info)
]
