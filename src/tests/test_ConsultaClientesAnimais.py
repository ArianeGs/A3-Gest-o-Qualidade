import unittest
from entities.Animal import Animal
from entities.Dono import Dono
import datetime

class TestConsultaClientesAnimais(unittest.TestCase):
    def setUp(self):
        self.dono1 = Dono(nome="Alice", sobrenome="Silva", cpf="123.456.789-00", numero_de_contato="123-456-7890", email="alice@example.com")
        self.animal1 = Animal(nome="Rex", especie="Cachorro", dono=self.dono1, sexo="Macho", data_nascimento="2023-01-01")
        
    def test_pesquisar_cliente_por_nome(self):
        resultado = self.animal1.nome
        self.assertEqual(resultado, "Rex")

    def test_pesquisar_cliente_por_especie(self):
        resultado = self.animal1.especie
        self.assertEqual(resultado, "Cachorro")

    def test_pesquisar_cliente_por_sexo(self):
        resultado = self.animal1.sexo
        self.assertEqual(resultado, "Macho")

    def test_pesquisar_cliente_por_data_nascimento(self):
        resultado = self.animal1.data_nascimento.strftime("%Y-%m-%d")
        self.assertEqual(resultado, "2023-01-01")

if __name__ == "__main__":
    unittest.main()
