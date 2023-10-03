from django.urls import path

from empresa.views import index, cadastro, funcionario, criar_funcionario, exportar_csv, grafico

urlpatterns = [
    path("index", index, name='index'),
    path("cadastro", cadastro, name='cadastro'),
    path("funcionarios", funcionario, name='funcionarios'),
    path("criarfuncionario", criar_funcionario, name='criarfuncionario'),
    path('exportar_csv', exportar_csv, name='exportar_csv'),
    path('grafico', grafico, name='grafico'),
]