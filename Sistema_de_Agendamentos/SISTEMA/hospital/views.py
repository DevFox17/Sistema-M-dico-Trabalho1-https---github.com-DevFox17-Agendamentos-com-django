from django.shortcuts import render, redirect
from .models import Medico, Paciente, Agendamento, Cancelamento
from .forms import AgendamentoForm
from django.shortcuts import get_object_or_404
from .models import RegistroExclusao

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

def deletar_paciente(request, paciente_id):
    paciente = get_object_or_404 (Paciente, id=paciente_id)

    if request.method == 'POST':
        motivo = request.POST['motivo']
        RegistroExclusao.objects.create(paciente=paciente, motivo=motivo)
        paciente.delete()
        return redirect('listar_agendamentos')

    return render(request, 'confirmar_exclusao.html', {'paciente': paciente})
 