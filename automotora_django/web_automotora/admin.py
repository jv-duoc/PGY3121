from django.contrib import admin

from web_automotora.models import Auto,Tipo

# Register your models here.

@admin.register(Auto)
class AutoAdmin(admin.ModelAdmin):
    pass

@admin.register(Tipo)
class TipoAdmin(admin.ModelAdmin):
    pass