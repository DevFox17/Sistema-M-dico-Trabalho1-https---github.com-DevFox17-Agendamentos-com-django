from django.db import models
from django.core.exceptions import ValidationError

class Medico(models.Model):
    nome = models.CharField(max_length=50)
    especialidade = models.CharField(max_length=50)    # esse é o modelo do medico
                                                       # ele vai aparecer na pagina de agendamento quando configurado no admin
    def __str__(self):
        return self.nome

class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()         # a mesma coisa do medico
    telefone = models.CharField(max_length=10)

    def __str__(self):
        return self.nome
    
class RegistroExclusao(models.Model):                                 # esse é o modelo do registro de exclusao
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)  # ele pega o paciente la do admin e deleta (mas aidna tenho que corrigir isso
    motivo = models.TextField()                                       # depois pq ele ta apagando o paciente la do admin ao invés de apagar só o agendamento)
    data_exclusao = models.DateField(auto_now_add=True)

    def __str__(self):
        return f" Paciente: {self.Paciente.nome} - Motivo: {self.motivo}"    # esse é o que vai aparecer na pagina de exclusao

class Cancelamento(models.Model):                           # esse é o modelo do cancelamento
    cancelamento = models.BooleanField(default=False)       # ele só cancela o agendamento mesmo, mais nada kakaka

    def __str__(self):
        return "Cancelado" if self.cancelado else "Ativo" 
    
    def __str__(self):
        return f"{self.medico} - {self.paciente} - {self.data_hora}"
class Agendamento(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)       # aqui funciona o agendemento
    data_hora = models.DateTimeField()
    cancelamento = models.ForeignKey(Cancelamento, null=True, blank=True, on_delete=models.SET_NULL)

    def clean(self):
        if Agendamento.objects.filter(medico=self.medico, data_hora=self.data_hora).exists():      # se o medico tiver um agendamento nessa data e hora
            raise ValidationError("O médico ja possui um agendamento nessa data e hora.\nPor favor agende pelo menos 10 minutos depois.")

    def __str__(self):
        return f"{self.medico} - {self.paciente} - {self.data_hora}"
    
    def save(self, *args, **kwargs):    # ele salva o agendamento
        self.full_clean()
        super().save(*args, **kwargs)




# Esse abaixo foi o projeto inicial kkkaka


# BoasVindas = "Olá seja bem vindo a Medic Mais! Selecione uma opçao para prosseguir: "
# print(BoasVindas)
# 
# opcoes = ""
# dastasDeAgendamentos = ['12.01', '25.02', '28.02']
# 
# while opcoes != "Sair":
#     print("1. Agendar")
#     print("2. Ver médicos disponiveis")
#     print("Sair")
# 
#     opcao = input("Digite uma opção: ")
# 
#     if opcao == "1":
#         nome = input("Digite seu nome: ")
#         DataDeNascimento = input("Digite sua data de nascimento: ")
#         cpf = input("Digite seu CPF: ")
# 
#         print(f"Datas disponiveis: {dastasDeAgendamentos}")
#         Data = input("Selecione a data do seu agendamento")
# 
#         print("Sua data foi agendada com sucesso!")
#         break
# 
#     elif opcao == "2":
#         Medicos_Lista = ['André', 'Marcos', 'Paulo']
#         print(f"Os medicos disponiveis sãp: {Medicos_Lista}")
# 
#     elif opcao == "Sair":
#         print("Obrigado. Volte sempre!")
#         break
# 
#     else:
#         print("Opção inválida, tente novamente!")