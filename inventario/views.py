from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from inventario.models import Equipamento, Reserva
from .serializers import EquipamentoSerializer, ReservaSerializer

# Create your views here.    

# -- VIEWS EQUIPAMENTOS --
@api_view(['GET'])
def lista_equipamentos_api(request):
    queryset = Equipamento.objects.all()
    status_filtro  = request.query_params.get('status', None)

    if status_filtro is not None:
        queryset = queryset.filter(status__iexact=status_filtro)

    serializer = EquipamentoSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def criar_equipamento_api(request):
    serializer = EquipamentoSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deletar_equipamento_api(request, pk):
    equipamento = get_object_or_404(Equipamento, pk=pk)
    equipamento.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT', 'PATCH'])
def atualizar_equipamento_api(request, pk):
    equipamento = get_object_or_404(Equipamento, pk=pk)
    
    serializer = EquipamentoSerializer(equipamento, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# -- VIEWS RESERVAS --
@api_view(['GET'])
def lista_reservas_api(request):
    queryset = Reserva.objects.all()
    serializer = ReservaSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def criar_reserva_api(request):
    serializer = ReservaSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        equipamento_id = request.data.get('equipamento')
        equipamento = get_object_or_404(Equipamento, pk=equipamento_id)
        
        if equipamento.status != 'disponivel':
            return Response({'error': 'Equipamento não disponível para reserva.'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer.save()
        equipamento.status = 'emprestado'
        equipamento.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deletar_reserva_api(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    equipamento = reserva.equipamento
    equipamento.status = 'disponivel'
    equipamento.save()
    reserva.delete()
    return Response({"message": "Equipamento devolvido com sucesso."}, status=status.HTTP_204_NO_CONTENT)