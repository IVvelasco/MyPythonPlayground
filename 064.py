# Level 064

# -------------------------------------
# -- QUANTO TEMPO PARA APOSENTAR-SE  --
# --      FEMININO E MASCULINO       --
# -------------------------------------

"""
Análise simples de aposentadoria, partindo do princípio de que os funcionários irão aposentar-se por idade e não por contribuição
"""

class funcionarioM: 
    def __init__(self, nome, sobrenome, sexo, cpf, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.sexo = sexo
        self.cpf = cpf 
        self.idade = idade

        if idade >= 60:
            aposentadoria = 65
            print(f"O funcionário {nome} {sobrenome} está para aposentar-se daqui a {aposentadoria - idade} ano(s)")

class funcionarioF: 
    def __init__(self, nome, sobrenome, sexo, cpf, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.sexo = sexo
        self.cpf = cpf 
        self.idade = idade

        if idade >= 60:
            aposentadoria = 62
            print(f"A funcionária {nome} {sobrenome} está para aposentar-se daqui a {aposentadoria - idade} ano(s)")
            
        
if __name__ == "__main__":
    pessoa0 = funcionarioM("João", "da Silva","M","000.000.000-00", 60)
    pessoa1 = funcionarioM("Roberto", "Costa", "M", "000.000.000-00", 64)
    pessoa2 = funcionarioM("Ribamar", "Salgado", "M", "000.000.000-00", 58)
    pessoa3 = funcionarioM("Geovane", "Velasco", "M", "000.000.000-00", 34)
    pessoa4 = funcionarioM("Marcelo", "Araújo", "M", "000.000.000-00", 33)
    pessoa5 = funcionarioM("Paulo", "Silva", "M", "000.000.000-00", 18)
    pessoa6 = funcionarioF("Rosa", "da Conceição", "F", "000.000.000-00", 61)
    pessoa7 = funcionarioF("Maria", "da Silva", "F", "000.000.000-00", 39)
    pessoa8 = funcionarioF("Ana", "Marinho", "F", "000.000.000-00", 60)