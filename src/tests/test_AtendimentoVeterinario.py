import unittest
from entities.Animal import Animal
from entities.Dono import Dono
from entities.AtendimentoVeterinario import AtendimentoVeterinario, AtendimentoManager
import datetime

class TestAtendimentoVeterinario(unittest.TestCase):
    def setUp(self):
        self.dono = Dono(nome="Alice", sobrenome="Silva", cpf="123.456.789-00", numero_de_contato="123-456-7890", email="alice@example.com")
        self.animal = Animal(nome="Rex", especie="Cachorro", dono=self.dono, sexo="Macho", data_nascimento="2023-01-01")
        self.atendimento_manager = AtendimentoManager()

    def test_agendar_consulta_para_animal_cadastrado(self):
        dono = Dono(nome="João", sobrenome="Silva", cpf="123.456.789-00", numero_de_contato="123456789", email="joao@example.com")
        animal = Animal(nome="Bolinha", especie="Cachorro", dono=dono, sexo="Macho", data_nascimento="2023-01-01")
        atendimento = AtendimentoVeterinario(animal, "2023-12-01", "Febre", "Diagnóstico")

        # Primeiro agendamento bem-sucedido
        self.assertTrue(self.atendimento_manager.agendar_consulta(atendimento))

        # Tentativa de agendar o mesmo animal novamente (deve falhar)
        self.assertFalse(self.atendimento_manager.agendar_consulta(atendimento))

    def test_validar_disponibilidade_do_veterinario(self):
        # Simulando a disponibilidade do veterinário no horário especificado
        horario_disponivel = datetime.datetime.now() + datetime.timedelta(hours=1)
        atendimento = AtendimentoVeterinario(animal=self.animal, data=horario_disponivel.strftime("%Y-%m-%d %H:%M"), sintomas="Dor de estômago", diagnostico="Indisposição")
        self.assertTrue(self.atendimento_manager.validar_disponibilidade(atendimento))

    def test_nao_agendar_consulta_para_datas_passadas(self):
        data_passada = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M")
        atendimento = AtendimentoVeterinario(animal=self.animal, data=data_passada, sintomas="Dor de estômago", diagnostico="Indisposição")
        self.assertFalse(self.atendimento_manager.agendar_consulta(atendimento))

if __name__ == "__main__":
    unittest.main()

