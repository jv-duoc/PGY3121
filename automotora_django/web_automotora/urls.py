from web_automotora import views
from django.urls import path


urlpatterns = [
    path('', views.inicio),
    path('info',views.info)
]