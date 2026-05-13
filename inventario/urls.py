from django.urls import path
from . import views 

urlpatterns = [
    path('api/equipamentos/', views.lista_equipamentos_api, name='lista_equipamentos_api'),
    path('api/equipamentos/criar/', views.criar_equipamento_api, name='criar_equipamento_api'),
    path('api/equipamentos/deletar/<int:pk>/', views.deletar_equipamento_api, name='deletar_equipamento_api'),
    path('api/equipamentos/atualizar/<int:pk>/', views.atualizar_equipamento_api, name='atualizar_equipamento_api'),
    path('api/reservas/', views.lista_reservas_api, name='lista_reservas_api'),
    path('api/reservas/criar/', views.criar_reserva_api, name='criar_reserva_api'),
    path('api/reservas/deletar/<int:pk>/', views.deletar_reserva_api, name='deletar_reserva_api'),
]