from django.contrib import admin
from .models import Carreira

# Register your models here.
class ListandoCarreira(admin.ModelAdmin):
    list_display = ('id', 'nome_empresa_fonetico','nome_empresa','cargo','funcao','inicio','fim','empresa_atual')
    list_display_links = ('id','nome_empresa_fonetico','cargo',)
    search_fields = ('nome_empresa_fonetico',)
    list_per_page = 10
    list_filter = ('cargo','nome_empresa_fonetico',)
    
    
admin.site.register(Carreira, ListandoCarreira)