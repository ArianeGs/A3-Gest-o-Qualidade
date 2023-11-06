import datetime

class AtendimentoVeterinario:
    def __init__(self, animal, data, sintomas, diagnostico):
        self.animal = animal
        self.data = datetime.datetime.strptime(data, "%Y-%m-%d %H:%M")  # Convertendo a string para um objeto datetime
        self.sintomas = sintomas
        self.diagnostico = diagnostico

    def __str__(self):
        return f"Consulta para {self.animal.nome} ({self.animal.dono.nome}): {self.data.strftime('%Y-%m-%d %H:%M')} - Sintomas: {self.sintomas}"

class AtendimentoManager:
    def __init__(self):
        self.atendimentos_agendados = []

    def agendar_consulta(self, atendimento):
        # Validar a disponibilidade do veterinário
        if self.validar_disponibilidade(atendimento):
            # Verificar se já existe um atendimento agendado para a mesma data
            for agendamento in self.atendimentos_agendados:
                if agendamento.data == atendimento.data:
                    return False  # Já existe um agendamento para esta data

            # Adicionar o atendimento à lista de atendimentos agendados
            self.atendimentos_agendados.append(atendimento)
            return True  # Agendamento bem-sucedido
        else:
            return False  # Não há disponibilidade para a data do atendimento

    def validar_disponibilidade(self, atendimento):
        # Obter a data atual
        data_atual = datetime.datetime.now()

        # Comparar as datas
        if atendimento.data > data_atual:
            return True  # Disponibilidade para a data do atendimento
        else:
            return False  # Não há disponibilidade para a data do atendimento
    
    def visualizar_agenda_por_data(self, data):
        consultas_agendadas = []
        for atendimento in self.atendimentos_agendados:
            if atendimento.data.strftime("%Y-%m-%d") == data.strftime("%Y-%m-%d"):
                consultas_agendadas.append(atendimento)
        return consultas_agendadas
    
    def listar_consultas_agendadas(self):
        consultas_agendadas = []
        for atendimento in self.atendimentos_agendados:
            consultas_agendadas.append(str(atendimento))
        return consultas_agendadas
    
    def encontrar_atendimento_por_animal(self, animal):
        for atendimento in self.atendimentos_agendados:
            if atendimento.animal == animal:
                return atendimento
        return None

    def editar_atendimento(self, animal, nova_data, novos_sintomas):
        atendimento = self.encontrar_atendimento_por_animal(animal)
        if atendimento:
            atendimento.data = datetime.datetime.strptime(nova_data, "%Y-%m-%d %H:%M")  # Convertendo a string para um objeto datetime
            atendimento.sintomas = novos_sintomas
            return True
        return False

    def cancelar_atendimento(self, animal):
        atendimento = self.encontrar_atendimento_por_animal(animal)
        if atendimento:
            self.atendimentos_agendados.remove(atendimento)
            return True
        return False

    def __str__(self):
        return f"Atendimentos agendados: {[str(atendimento) for atendimento in self.atendimentos_agendados]}"
    
    def __init__(self):
        self.atendimentos_agendados = []