# Level 060

# -------------------------------
# -- SUA IDADE DAQUI A 10 ANOS -- 
# -------------------------------

nome = input("Insira seu nome ou apelido: ")
nascimento = int(input("Insira seu ano de nascimento: "))
ano_atual = int(input("Insira o ano em que estamos: "))
idade = ano_atual - nascimento 
print(f"{nome}, daqui a 10 anos você terá: {idade + 10} anos")