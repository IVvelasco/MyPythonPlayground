# Level 062

# ------------------------------------
# -- FUNCIONÁRIOS PARA APOSENTAR-SE --
# ------------------------------------

"""
Análise simples de aposentadoria, partindo do princípio de que os funcionários irão aposentar-se por idade e não por contribuição
"""

class funcionario: 
    def __init__(self, nome, sobrenome, idade, sexo, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.sexo = sexo
        self.cpf = cpf 
        self.idade = idade

        if idade >= '60':
            print(f"O funcionário {nome} está para aposentar-se")
        
if __name__ == "__main__":
    pessoa0 = funcionario("João", "da Silva","M","000.000.000-00", '60')
    pessoa1 = funcionario("Roberto", "Costa", "M", "000.000.000-00", '64')
