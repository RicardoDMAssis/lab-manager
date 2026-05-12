from django.urls import path
from . import views 

urlpatterns = [
    path('api/equipamentos/', views.lista_equipamentos_api, name='lista_equipamentos_api'),
] 