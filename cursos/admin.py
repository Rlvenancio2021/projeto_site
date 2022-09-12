from django.contrib import admin
from .models import Curso

# Register your models here.
class ListandoCurso(admin.ModelAdmin):
    list_display = ('id','nome_instituicao','status','categoria','area_estudo','linguagem','nome_curso','tecnologia','inicio','conclusao','url_certificado')
    list_display_links = ('id','nome_instituicao','linguagem','url_certificado',)
    list_filter = ('nome_instituicao','area_estudo','linguagem','categoria',)
    list_per_page =15
    search_fields = ('linguagem','tecnologia',)
    
admin.site.register(Curso, ListandoCurso)