from django.urls import path

from web import views

urlpatterns = [
    path('', views.inicio,name='inicio'),
    path('login',views.login_vista,name='login'),
    path('logout',views.salir,name="logout"),
    path('mi-cuenta',views.cuenta,name='cuenta')
]
