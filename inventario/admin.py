from django.contrib import admin
from .models import Laboratorio, Equipamento, Reserva

admin.site.register(Laboratorio)
admin.site.register(Reserva)

@admin.register(Equipamento)
class EquipamentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'laboratorio', 'status')
    list_filter = ('laboratorio', 'status')
    search_fields = ('nome', 'laboratorio__nome')