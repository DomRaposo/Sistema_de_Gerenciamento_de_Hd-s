# BackEnd/legado_hdm_project/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # Rota de Administração do Django
    path('admin/', admin.site.urls),
    
    # Rota de Login JWT (POST para obter o token)
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    # Rota de Refresh JWT (POST para renovar o token)
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # 💡 INCLUI TODAS AS ROTAS DO SEU APP 'hdm_manager' com o prefixo 'api/v1/'
    path('api/v1/', include('hdm_manager.urls')), 
]