# Level 50 

# ------------------------------
# -- USANDO CLASSES E MÉTODOS --
# ------------------------------

"""
Exercício retirado do site < treinaweb.com.br > 
"""

class Pessoa: 
    def __init__(self, nome, sexo, cpf, ativado):
        self.nome = nome
        self.sexo = sexo
        self.cpf = cpf 
        self.ativado = ativado

    def desativar(self):
        self.ativado == False
        print("A pessoa foi desativada com sucesso")

if __name__ == "__main__":
    pessoa1 = Pessoa("João", "M", "000.000.000-00", True)
    pessoa1.desativar()