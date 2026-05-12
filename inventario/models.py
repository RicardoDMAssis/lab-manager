from django.db import models

# Create your models here.

class Laboratorio(models.Model):
    nome = models.CharField(max_length=100)
    localizacao = models.CharField(max_length=100)
    capacidade = models.IntegerField()

    def __str__(self):
        return self.nome
    
class Equipamento(models.Model):

    STATUS_CHOICES = [
        ('disponivel', 'Disponível'),
        ('emprestado', 'Emprestado'),
        ('manutencao', 'Em Manutenção'),
    ]

    nome = models.CharField(max_length=100)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE, related_name='equipamentos')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='disponivel')

    def __str__(self):
        return self.nome
    
class Reserva(models.Model):
    usuario = models.CharField(max_length=100)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.SET_NULL, null=True, blank=True, related_name='reservas')
    equipamento = models.ManyToManyField(Equipamento, blank=True)
    data_reserva = models.DateTimeField(auto_now_add=True)
    data_devolucao = models.DateTimeField(null=True, blank=True)
    finalidade = models.TextField()

    def __str__(self):
        return f"Reserva de {self.usuario} - {self.data_reserva.strftime('%Y-%m-%d %H:%M:%S')}"