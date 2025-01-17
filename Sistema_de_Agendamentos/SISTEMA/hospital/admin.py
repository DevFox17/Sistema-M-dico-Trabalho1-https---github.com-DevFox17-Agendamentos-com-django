from django.contrib import admin
from .models import Medico, Paciente, Agendamento

admin.site.register(Medico)
admin.site.register(Paciente)
admin.site.register(Agendamento)
