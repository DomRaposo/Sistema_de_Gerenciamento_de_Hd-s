from django.db import models
from django.utils import timezone
from .managers import HDManager

class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    contato = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nome

class HD(models.Model):
    
    STATUS_CHOICES = [
        ('LIVRE', 'Livre (Aguardando Projeto)'),
        ('EM_USO', 'Em Uso (Projeto Ativo)'),
        ('ARQUIVADO', 'Arquivado (Dados Completos)'),
        ('MANUTENCAO', 'Manutenção/Defeito'),
    ]

    nome_hd = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100, unique=True)
    tamanho_total_gb = models.DecimalField(max_digits=8, decimal_places=2)
    tamanho_livre_gb = models.DecimalField(max_digits=8, decimal_places=2) # Será atualizado ou calculado
    localizacao = models.CharField(max_length=255) # Ex: "Prateleira A, Gaveta 3"
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='LIVRE')
    data_cadastro = models.DateTimeField(default=timezone.now)
    
    objects = HDManager()


    def __str__(self):
        return f"{self.nome_hd} ({self.serial_number})"

class Trabalho(models.Model):
    titulo = models.CharField(max_length=255)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_inicio = models.DateField(default=timezone.now)
    data_fim = models.DateField(blank=True, null=True)
    descricao = models.TextField(blank=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.titulo} - {self.cliente.nome}"

class ConteudoPastaRaiz(models.Model):
    nome_pasta = models.CharField(max_length=255)
    hd = models.ForeignKey(HD, on_delete=models.CASCADE)
    trabalho = models.ForeignKey(Trabalho, on_delete=models.CASCADE)
    caminho_raiz = models.CharField(max_length=500) # Ex: "D:/" ou "/Volumes/ProjetoX/"
    tamanho_ocupado_gb = models.DecimalField(max_digits=8, decimal_places=2)
    data_adicao = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "Conteúdo/Pasta Raiz"
        verbose_name_plural = "Conteúdos/Pastas Raiz"

    def __str__(self):
        return f"{self.nome_pasta} em {self.hd.nome_hd}"