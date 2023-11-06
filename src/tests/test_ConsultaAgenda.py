import unittest
from entities.Animal import Animal
from entities.Dono import Dono
from entities.AtendimentoVeterinario import AtendimentoVeterinario, AtendimentoManager
import datetime

class ConsultaAgenda(unittest.TestCase):
    def setUp(self):
        self.dono = Dono(nome="Alice", sobrenome="Silva", cpf="123.456.789-00", numero_de_contato="123-456-7890", email="alice@example.com")
        self.animal = Animal(nome="Rex", especie="Cachorro", dono=self.dono, sexo="Macho", data_nascimento="2023-01-01")
        self.atendimento_manager = AtendimentoManager()

    def test_visualizar_agenda_por_data(self):
        data_consulta = "2023-11-25 14:30"
        atendimento = AtendimentoVeterinario(animal=self.animal, data=data_consulta, sintomas="Dor de estômago", diagnostico="Indisposição")
        self.assertTrue(self.atendimento_manager.agendar_consulta(atendimento))
        consultas_agendadas = self.atendimento_manager.visualizar_agenda_por_data(datetime.datetime.strptime(data_consulta, "%Y-%m-%d %H:%M"))
        self.assertIn(atendimento, consultas_agendadas)

    def test_listar_consultas_agendadas(self):
        animal1 = Animal(nome="Max", especie="Gato", dono=self.dono, sexo="Fêmea", data_nascimento="2022-05-15")
        atendimento1 = AtendimentoVeterinario(animal=animal1, data="2023-11-15 14:30", sintomas="Febre", diagnostico="Resfriado")
        self.atendimento_manager.agendar_consulta(atendimento1)

        atendimento2 = AtendimentoVeterinario(animal=self.animal, data="2023-11-20 16:00", sintomas="Dor de ouvido", diagnostico="Infecção")
        self.atendimento_manager.agendar_consulta(atendimento2)

        consultas_agendadas = self.atendimento_manager.listar_consultas_agendadas()
        self.assertEqual(len(consultas_agendadas), 2)
        self.assertIn(str(atendimento1), consultas_agendadas)
        self.assertIn(str(atendimento2), consultas_agendadas)

    def test_editar_atendimento(self):
        atendimento = AtendimentoVeterinario(animal=self.animal, data="2023-11-25 10:00", sintomas="Dor de estômago", diagnostico="Indisposição")
        self.atendimento_manager.agendar_consulta(atendimento)

        nova_data = "2023-11-25 14:30"
        novos_sintomas = "Vômitos"
        self.assertTrue(self.atendimento_manager.editar_atendimento(self.animal, nova_data, novos_sintomas))
        atendimento_editado = self.atendimento_manager.encontrar_atendimento_por_animal(self.animal)
        nova_data_obj = datetime.datetime.strptime(nova_data, "%Y-%m-%d %H:%M")
        self.assertEqual(atendimento_editado.data, nova_data_obj)
        self.assertEqual(atendimento_editado.sintomas, novos_sintomas)

    def test_cancelar_atendimento(self):
        atendimento = AtendimentoVeterinario(animal=self.animal, data="2023-11-28 11:00", sintomas="Dor de estômago", diagnostico="Indisposição")
        self.atendimento_manager.agendar_consulta(atendimento)

        self.assertTrue(self.atendimento_manager.cancelar_atendimento(self.animal))
        atendimento_cancelado = self.atendimento_manager.encontrar_atendimento_por_animal(self.animal)
        self.assertIsNone(atendimento_cancelado)

if __name__ == "__main__":
    unittest.main()
