from django import forms
from .models import Pessoa, Funcionario, Cargo



class PessoaForm(forms.ModelForm):
   
    nome = forms.CharField(label='Nome', required=True)
    sobrenome = forms.CharField(label='Sobrenome', required=True)
    idade = forms.IntegerField(label='Idade', required=True)

    class Meta:
        model = Pessoa
        fields = ['nome', 'sobrenome', 'idade']


class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nome', 'sobrenome', 'idade', 'matricula', 'cargo', 'salario', 'ativo']

    nome = forms.CharField(label='Nome', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    sobrenome = forms.CharField(label='Sobrenome', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    idade = forms.IntegerField(label='Idade', required=True, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    matricula = forms.CharField(label='Matrícula', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cargo = forms.ModelChoiceField(queryset=Cargo.objects.all(), empty_label="Selecione um cargo", widget=forms.Select(attrs={'class': 'form-control'}))
    salario = forms.DecimalField(label='Salário', required=True, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    ativo = forms.BooleanField(initial=True, required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))