from django.db import models
from django.utils import timezone

# Create your models here.


class Cargo(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Pessoa(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    idade = models.IntegerField()
    criado_em = models.DateTimeField(auto_now_add=True, blank=True, null=True)


    class Meta:
        ordering = ['nome']
        verbose_name = 'pessoa'
       


    def __str__(self):
        return self.nome + ' ' + self.sobrenome


class Funcionario(Pessoa):
    matricula = models.CharField(max_length=50)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    salario = models.DecimalField(max_digits=8, decimal_places=2)
    ativo = models.BooleanField(default=True)
    data_contratacao = models.DateField(default=timezone.now)  


    def esta_ativo(self):
        return self.ativo
    
    
    def get_salario(self):
        return self.salario
    
    def set_salario(self, salario):
        self.salario = salario

    def get_cargo(self):
        return self.cargo    
    
    class Meta:
        ordering = ['matricula']
        verbose_name = 'funcionario'
        
  
    def __str__(self):
        return f"{self.matricula} - {self.nome} - {self.sobrenome}"
