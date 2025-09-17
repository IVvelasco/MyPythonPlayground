# Level 063

# ------------------------------------
# -- QUANTO TEMPO PARA APOSENTAR-SE --
# ------------------------------------

"""
Análise simples de aposentadoria, partindo do princípio de que os funcionários irão aposentar-se por idade e não por contribuição
"""

class funcionario: 
    def __init__(self, nome, sobrenome, sexo, cpf, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.sexo = sexo
        self.cpf = cpf 
        self.idade = idade

        if idade >= 60:
            aposentadoria = 65
            print(f"O funcionário {nome} {sobrenome} está para aposentar-se daqui a {aposentadoria - idade} ano(s)")
        
if __name__ == "__main__":
    pessoa0 = funcionario("João", "da Silva","M","000.000.000-00", 60)
    pessoa1 = funcionario("Roberto", "Costa", "M", "000.000.000-00", 64)
    pessoa2 = funcionario("Ribamar", "Salgado", "M", "000.000.000-00", 58)
    pessoa3 = funcionario("Geovane", "Velasco", "M", "000.000.000-00", 34)
    pessoa4 = funcionario("Marcelo", "Araújo", "M", "000.000.000-00", 33)
    pessoa5 = funcionario("Paulo", "Silva", "M", "000.000.000-00", 18)
    