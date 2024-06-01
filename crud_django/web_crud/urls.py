from django.urls import path

from web_crud import views

urlpatterns = [
    path('',views.lista),
    path('nueva',views.nueva),
    path('borrar/<int:id>',views.borrar)
]