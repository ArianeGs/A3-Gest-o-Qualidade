import datetime

class Animal:
    def __init__(self, nome, especie, dono, sexo, data_nascimento):
        if nome and nome.strip():  # Verifica se o nome não é vazio ou contém apenas espaços em branco
                self.nome = nome
        else:
            self.nome = None
        self.especie = especie
        self.dono = dono
        self.sexo = sexo
        try:
            self.data_nascimento = datetime.datetime.strptime(data_nascimento, "%Y-%m-%d").date()
        except ValueError:
            self.data_nascimento = None