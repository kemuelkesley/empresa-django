from django.contrib import admin
from empresa.models import Cargo ,Pessoa, Funcionario


class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'idade',)
    list_display_links = ('nome',)


class FuncionarioAdmin(admin.ModelAdmin):
    list_display = (
        'matricula', 
        'nome', 
        'cargo', 
        'salario', 
        'ativo', 
        'criado_em',
        'data_contratacao',
    )
    llist_filter = ('cargo', 'ativo',)


admin.site.register(Cargo)
admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(Funcionario,FuncionarioAdmin)