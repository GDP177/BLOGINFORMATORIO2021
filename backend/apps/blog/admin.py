from django.contrib import admin
from .models import Noticia


class NoticiaAdmin(admin.ModelAdmin):
	list_display = ('titulo', 'autor', 'fecha_creacion')
	list_filter = ('autor',)
# Register your models here.
admin.site.register(Noticia, NoticiaAdmin)