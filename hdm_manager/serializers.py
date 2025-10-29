from rest_framework import serializers
from .models import HD, Trabalho, Cliente, ConteudoPastaRaiz


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__' 


class TrabalhoSerializer(serializers.ModelSerializer):
    
    cliente_nome = serializers.ReadOnlyField(source='cliente.nome') 
    
    class Meta:
        model = Trabalho
        
        fields = ['id', 'titulo', 'cliente', 'cliente_nome', 'data_inicio', 'data_fim', 'descricao', 'ativo']


class HDSerializer(serializers.ModelSerializer):
    
    
    espaco_ocupado = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    espaco_livre_calculado = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = HD
        
        fields = '__all__' 
        



class ConteudoPastaRaizSerializer(serializers.ModelSerializer):
    
    trabalho_titulo = serializers.ReadOnlyField(source='trabalho.titulo')
    hd_nome = serializers.ReadOnlyField(source='hd.nome_hd')

    class Meta:
        model = ConteudoPastaRaiz
        fields = '__all__'
       