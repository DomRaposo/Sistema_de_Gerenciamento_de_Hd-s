from rest_framework import viewsets
from django.db.models import Q 

class HDViewSet(viewsets.ModelViewSet):
    serializer_class = HDSerializer
    
    def get_queryset(self):
        queryset = HD.objects.all().order_by('nome_hd')
        search_term = self.request.query_params.get('search', None) 

        if search_term:
            queryset = queryset.filter(
                Q(nome_hd__icontains=search_term) |
                Q(serial_number__icontains=search_term) |
                Q(localizacao__icontains=search_term) |
                Q(status__icontains=search_term)
            ).distinct()

        return queryset
    

class TrabalhoViewSet(viewsets.ModelViewSet):
    serializer_class = TrabalhoSerializer

    def get_queryset(self):
        queryset = Trabalho.objects.all().order_by('-data_inicio')
        search_term = self.request.query_params.get('search', None)

        if search_term:
            
            queryset = queryset.filter(
                Q(titulo__icontains=search_term) |
                Q(cliente__nome__icontains=search_term) 
            ).distinct()

        return queryset
    
    

class ConteudoPastaRaizViewSet(viewsets.ModelViewSet):
    queryset = ConteudoPastaRaiz.objects.all().order_by('nome_pasta')
    serializer_class = ConteudoPastaRaizSerializer
    
    
    def get_queryset(self):
        queryset = ConteudoPastaRaiz.objects.all().order_by('nome_pasta')
        search_term = self.request.query_params.get('search', None)

        if search_term:
            queryset = queryset.filter(
                Q(nome_pasta__icontains=search_term) |
                Q(trabalho__titulo__icontains=search_term) | 
                Q(hd__nome_hd__icontains=search_term) 
            ).distinct()

        return queryset