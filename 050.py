# Level 50 

# -----------------------
# -- DEFININDO CLASSES --
# -----------------------

"""
Exercício retirado do site < treinaweb.com.br > 
"""

class Pessoa: 
    def __init__(self, nome, sexo, cpf):
        self.nome = nome
        self.sexo = sexo
        self.cpf = cpf 

if __name__ == "__main__":
    pessoa1 = Pessoa("João", "M", "000.000.000-00")
    print(f"Nome:{pessoa1.nome}, Sexo: {pessoa1.sexo} e CPF: {pessoa1.cpf}")