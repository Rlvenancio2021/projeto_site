from django.contrib import admin
from .models import Graduacao

# Register your models here.
class ListandoGraduacao(admin.ModelAdmin):
    list_display = ('id', 'nome_instituicao','nivel','status','categoria','nome_curso','inicio','conclusao')
    list_display_links = ('id','nome_instituicao','nome_curso',)
    list_filter = ('nivel','status','categoria',)
    list_per_page = 15
    
admin.site.register(Graduacao, ListandoGraduacao)