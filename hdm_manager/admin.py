# hdm_manager/admin.py
from django.contrib import admin
from .models import Cliente, HD, Trabalho, ConteudoPastaRaiz

admin.site.register(Cliente)
admin.site.register(HD)
admin.site.register(Trabalho)
admin.site.register(ConteudoPastaRaiz)