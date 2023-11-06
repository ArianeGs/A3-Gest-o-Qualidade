class Dono:
    def __init__(self, nome, sobrenome, cpf, numero_de_contato, email):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
        self.numero_de_contato = numero_de_contato
        self.email = email

class DonoManager:
    def __init__(self):
        self.donos = []

    def cadastrar_dono(self, dono):
        if dono.nome and dono.numero_de_contato and self._email_unico(dono.email):
            self.donos.append(dono)
            return True
        return False

    def _email_unico(self, email):
        return email not in [dono.email for dono in self.donos]