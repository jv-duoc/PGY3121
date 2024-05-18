from django.contrib import admin

from web_automotora.models import Auto

# Register your models here.

@admin.register(Auto)
class AutoAdmin(admin.ModelAdmin):
    pass