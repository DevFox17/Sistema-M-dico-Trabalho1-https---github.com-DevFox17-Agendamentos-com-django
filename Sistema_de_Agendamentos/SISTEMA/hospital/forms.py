from django import forms
from .models import Agendamento

class AgendamentoForm(forms.ModelForm):          # criando um formulario
    class Meta:                                 # configurando o formulario
        model = Agendamento                     # qual modelo ele vai usar
        fields = ['medico', 'paciente', 'data_hora', 'cancelamento']    # quais campos ele vai usar
        widgets = {
            'data_hora': forms.DateTimeInput(attrs={'type': 'datetime-local'}),  # configurando o campo data_hora
        }