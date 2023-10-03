from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Pessoa, Funcionario
from .forms import PessoaForm, FuncionarioForm
import csv

import matplotlib.pyplot as plt
import io



def index(request):
    pessoas = Pessoa.objects.all()

    return render(request, "index.html", {'pessoas' : pessoas})



def cadastro(request):

    if request.method == 'POST':
        form = PessoaForm(request.POST)  # Crie um formulário com os dados do POST
        if form.is_valid():
            # Os dados do formulário são válidos, você pode acessá-los assim:
            nome = form.cleaned_data['nome']
            sobrenome = form.cleaned_data['sobrenome']
            idade = form.cleaned_data['idade']

            # Agora você pode criar um novo objeto Pessoa com esses dados
            nova_pessoa = Pessoa(nome=nome, sobrenome=sobrenome, idade=idade)
            nova_pessoa.save()  # Salvar a nova pessoa no banco de dados

            return redirect('index')  # Redirecionar após o cadastro bem-sucedido
    else:
        form = PessoaForm()
    return render(request, "cadastro.html", {'form' : form})



def funcionario(request):

    funcionarios_ativos = Funcionario.objects.filter(ativo=True)

    return render(request, "funcionarios.html", {"funcionarios" : funcionarios_ativos})


def criar_funcionario(request):

    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            funcionario = form.save()
            return redirect('funcionarios')
            # Faça o que for necessário após criar o funcionário
    else:
        form = FuncionarioForm()
    
    return render(request, 'criarfuncionario.html', {'form': form})


# Metodo que cria um arquivo CSV com os dados dos funcionários
def exportar_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="funcionarios.csv"'


     # Isso ajuda a definir a codificação UTF-8 no Excel

    writer = csv.writer(response)
    writer.writerow(['Nome','Sobrenome','Idade','Matricula','Cargo','Salario','Ativo','Contratação'])

    funcionarios = Funcionario.objects.all()

    for funcionario in funcionarios:


        writer.writerow([
            funcionario.nome, 
            funcionario.sobrenome, 
            funcionario.idade, 
            funcionario.matricula, 
            funcionario.cargo,
            funcionario.salario,
            funcionario.ativo,
            funcionario.data_contratacao
        ])

    return response



def grafico(request):
    funcionarios = Funcionario.objects.all()
    
    # Preparar dados para o gráfico
    nomes = [funcionario.nome for funcionario in funcionarios]
    salarios = [funcionario.salario for funcionario in funcionarios]

    # Criar o gráfico de barras
    plt.bar(nomes, salarios)
    plt.xlabel('Funcionário')
    plt.ylabel('Salário')
    plt.title('Salário dos Funcionários')
    
    # Salvar o gráfico em um objeto BytesIO
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    
    # Configurar a resposta HTTP para exibir o gráfico
    response = HttpResponse(buffer.read(), content_type='image/png')
    
    return response




