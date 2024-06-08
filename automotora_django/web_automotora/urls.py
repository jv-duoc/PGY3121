from web_automotora import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.inicio),
    path('info',views.info),
    path('tipos',views.listar_tipos)
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)