from django.contrib import admin
from cerveceria.models import Marca, Cerveza

class CervezaAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'marca', 'variedad', 'precio', 'cantidad')
	list_filter = ('marca', 'variedad')
	search_fields = ('nombre', 'variedad','precio', 'cantidad')

class MarcaAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'direccion')



# Register your models here.
admin.site.register(Marca, MarcaAdmin)
admin.site.register(Cerveza, CervezaAdmin)
