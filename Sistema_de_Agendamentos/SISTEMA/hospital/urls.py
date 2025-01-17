from django.urls import path
from . import views

urlpatterns = [
    
    path('agendamentos/', views.listar_agendamentos, name='listar_agendamentos'),
    path('agendamentos/novo/', views.criar_agendamento, name='criar_agendamento'),
]
    