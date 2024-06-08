from django.urls import path

from web_crud import views

urlpatterns = [
    path('',views.lista,name='lista'),
    path('nueva',views.nueva,name='nueva'),
    path('editar/<int:id>',views.editar,name='editar'),
    path('borrar/<int:id>',views.borrar,name='borrar'),
    path('login',views.view_login,name='login'),
    path('logout',views.salir,name='salir'),
    path('registro',views.view_registro,name='registro')
]