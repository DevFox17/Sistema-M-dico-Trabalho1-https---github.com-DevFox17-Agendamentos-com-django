from django.shortcuts import render, redirect
from .models import Medico, Paciente, Agendamento
from .forms import AgendamentoForm

def criar_agendamento(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_agendamentos')
    else:
        form = AgendamentoForm()
    return render(request, 'criar_agendamento.html', {'form': form})

def listar_agendamentos(request):
    agendamentos = Agendamento.objects.all()
    return render(request, 'listar_agendamentos.html', {'agendamentos': agendamentos})
 