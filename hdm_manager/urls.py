# hdm_manager/urls.py (Modifique o arquivo)
from rest_framework.routers import DefaultRouter
from .views import HDViewSet, TrabalhoViewSet, ClienteViewSet, ConteudoPastaRaizViewSet # 
router = DefaultRouter()
router.register(r'hds', HDViewSet, basename='hd')
router.register(r'trabalhos', TrabalhoViewSet, basename='trabalho')
router.register(r'clientes', ClienteViewSet, basename='cliente')
router.register(r'conteudo', ConteudoPastaRaizViewSet, basename='conteudo') # Adicione esta 


urlpatterns = router.urls