from django.contrib import admin
from .models import Carreira, Resumo_Carreira

# Register your models here.
class ListandoCarreira(admin.ModelAdmin):
    list_display = ('id', 'nome_empresa_fonetico','nome_empresa','cargo','funcao','inicio','fim','empresa_atual')
    list_display_links = ('id','nome_empresa_fonetico','cargo',)
    search_fields = ('nome_empresa_fonetico',)
    list_per_page = 10
    list_filter = ('cargo','nome_empresa_fonetico',)
    
    
admin.site.register(Carreira, ListandoCarreira)

class ListandoResumoCarreira(admin.ModelAdmin):
    list_display = ('id','titulo','resumo','data_inclusao','data_modificacao')
    list_display_links = ('id','titulo',)
    list_filter = ('titulo',)
    
admin.site.register(Resumo_Carreira, ListandoResumoCarreira)