from rest_framework import serializers
from .models import Equipamento, Reserva

class EquipamentoSerializer(serializers.ModelSerializer):
    laboratorio_nome = serializers.ReadOnlyField(source='laboratorio.nome')

    class Meta:
        model = Equipamento
        fields = ['id', 'nome', 'laboratorio', 'laboratorio_nome', 'status']


class ReservaSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Reserva
        fields = ['id', 'usuario', 'equipamento', 'data_reserva', 'data_devolucao']