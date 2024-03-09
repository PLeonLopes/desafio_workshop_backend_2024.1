from django.urls import path        # função default do django para usar o path
from . import views                 # importa tudo de views.py

urlpatterns = [
    path('', views.index, name='index') # '', porque é a única página | depois puxa a função do views.py pra fazer a conexão
]