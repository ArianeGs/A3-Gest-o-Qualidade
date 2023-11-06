import unittest
import datetime
from entities.Animal import Animal
from entities.Dono import Dono

class TestAnimal(unittest.TestCase):
    def setUp(self):
        self.dono = Dono(nome="Alice", sobrenome="Silva", cpf="123.456.789-00", numero_de_contato="123-456-7890", email="alice@example.com")

#    - Verificar se é possível cadastrar um novo animal para um cliente existente.
    def test_cadastrar_animal_com_todas_informacoes(self):
        animal = Animal(nome="Rex", especie="Cachorro", dono=self.dono, sexo="Macho", data_nascimento="2023-01-01")
        data_nascimento_esperada = datetime.date(2023, 1, 1)
        self.assertEqual(animal.nome, "Rex")
        self.assertEqual(animal.especie, "Cachorro")
        self.assertEqual(animal.dono, self.dono)
        self.assertEqual(animal.sexo, "Macho")
        self.assertEqual(animal.data_nascimento, data_nascimento_esperada)

#    - Garantir que o sistema não permita o cadastro de um animal sem um nome válido.
    def test_cadastrar_animal_sem_nome_valido(self):
        animal = Animal(nome="", especie="Cachorro", dono=self.dono, sexo="Macho", data_nascimento="2023-01-01")
        self.assertIsNone(animal.nome)

#   - Verificar se o sistema não aceita uma data de nascimento inválida para o animal.
    def test_cadastrar_animal_com_data_nascimento_invalida(self):
        animal = Animal(nome="Rex", especie="Cachorro", dono=self.dono, sexo="Macho", data_nascimento="invalida")
        self.assertIsNone(animal.data_nascimento)

#  - Garantir que o sistema permite associar um animal a um único dono.
    def test_associar_animal_a_um_unico_dono(self):
        outro_dono = Dono(nome="Bob", sobrenome="Johnson", cpf="987.654.321-00", numero_de_contato="987-654-3210", email="bob@example.com")
        animal = Animal(nome="Rex", especie="Cachorro", dono=self.dono, sexo="Macho", data_nascimento="2023-01-01")
        self.assertEqual(id(animal.dono), id(self.dono))
        animal.dono = outro_dono
        self.assertEqual(id(animal.dono), id(outro_dono))

if __name__ == "__main__":
    unittest.main()