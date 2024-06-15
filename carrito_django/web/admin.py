from django.contrib import admin

from web.models import Compra, DetalleCompra, Producto

# Register your models here.

admin.site.register(Producto)

admin.site.register(Compra)
admin.site.register(DetalleCompra)