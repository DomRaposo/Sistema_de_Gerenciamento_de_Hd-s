from django.db import models
from django.db.models import Sum, F
from django.db.models.functions import Coalesce
from django.apps import apps
 

class HDManager(models.Manager):
         
    def get_queryset(self):
        
        return super().get_queryset()
    
    
    def with_space_metrics(self):
        ConteudoPastaRaiz = apps.get_model('hdm_manager', 'ConteudoPastaRaiz')
        
        occupied_subquery = ConteudoPastaRaiz.objects.filter(
            hd=OuterRef('pk') # Filtra pela chave primária do HD externo
        ).values('hd').annotate(
            total_occupied=Sum('tamanho_ocupado_gb')
        ).values('total_occupied')[:1]
        
        
        return self.get_queryset().annotate(
            
            espaco_ocupado=Coalesce(
                Subquery(occupied_subquery, output_field=models.DecimalField()),
                models.Value(0.00, output_field=models.DecimalField())
            )
        ).annotate(
            
            espaco_livre_calculado=F('tamanho_total_gb') - F('espaco_ocupado')
        )