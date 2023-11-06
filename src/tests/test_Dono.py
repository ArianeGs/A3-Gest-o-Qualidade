import unittest
from entities.Dono import Dono, DonoManager

class TestDono(unittest.TestCase):
    def setUp(self):
        self.dono_manager = DonoManager()
# - Verificar se é possível cadastrar um novo cliente com todas as informações necessárias.
    def test_cadastrar_dono_com_todas_informacoes(self):
        dono = Dono(nome="Alice", sobrenome="Silva", cpf="123.456.789-00", numero_de_contato="123-456-7890", email="alice@example.com")
        self.assertTrue(self.dono_manager.cadastrar_dono(dono))

# - Garantir que o sistema não permita o cadastro de um cliente sem um nome válido.
    def test_cadastrar_dono_sem_nome_valido(self):
        dono = Dono(nome="", sobrenome="Silva", cpf="123.456.789-00", numero_de_contato="123-456-7890", email="alice@example.com")
        self.assertFalse(self.dono_manager.cadastrar_dono(dono))
# - Verificar se o sistema não aceita um número de telefone inválido durante o cadastro do cliente.
    def test_cadastrar_dono_com_numero_de_contato_invalido(self):
        dono = Dono(nome="Alice", sobrenome="Silva", cpf="123.456.789-00", numero_de_contato="", email="alice@example.com")
        self.assertFalse(self.dono_manager.cadastrar_dono(dono))
        
# - Garantir que o endereço de e-mail fornecido durante o cadastro seja único para cada cliente.
    def test_cadastrar_dono_com_email_duplicado(self):
        dono1 = Dono(nome="Alice", sobrenome="Silva", cpf="123.456.789-00", numero_de_contato="123-456-7890", email="alice@example.com")
        dono2 = Dono(nome="Bob", sobrenome="Johnson", cpf="987.654.321-00", numero_de_contato="987-654-3210", email="alice@example.com")
        self.assertTrue(self.dono_manager.cadastrar_dono(dono1))
        self.assertFalse(self.dono_manager.cadastrar_dono(dono2))

if __name__ == "__main__":
    unittest.main()
