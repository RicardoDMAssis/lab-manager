from rest_framework import serializers
from .models import Equipamento

class EquipamentoSerializer(serializers.ModelSerializer):
    laboratorio_nome = serializers.ReadOnlyField(source='laboratorio.nome')

    class Meta:
        model = Equipamento
        fields = ['id', 'nome', 'laboratorio', 'laboratorio_nome', 'status']