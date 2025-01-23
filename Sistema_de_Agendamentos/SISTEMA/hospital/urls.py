from django.urls import path
from . import views

urlpatterns = [
    
    path('agendamentos/', views.listar_agendamentos, name='listar_agendamentos'),
    path('agendamentos/novo/', views.criar_agendamento, name='criar_agendamento'),
    path('deletar_paciente/<int:paciente_id>/', views.deletar_paciente, name='deletar_paciente'),
]
    

    # tem que digitar no navegador http://127.0.0.1:8000/hospital/ ex:agendamentos ou agendamentos/novo
    # mas só de gitar /hospital/agendamentos o código já funciona