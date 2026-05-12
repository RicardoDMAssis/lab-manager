from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from inventario.models import Equipamento
from .serializers import EquipamentoSerializer

# Create your views here.    

@api_view(['GET'])
def lista_equipamentos_api(request):

    queryset = Equipamento.objects.all()

    status_filtro  = request.query_params.get('status', None)

    if status_filtro is not None:
        queryset = queryset.filter(status__iexact=status_filtro)

    serializer = EquipamentoSerializer(queryset, many=True)
    return Response(serializer.data)