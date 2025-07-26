# Level 047

#------------------------------------
# -- TESTANDO OPERADORES TERNÁRIOS --
# --     USER LOGIN OR LOGOUT      --
# -----------------------------------

def main():
    usuario = 'nome'
    senha = int(12345678)
    print("------------------------------")
    print("Bem-Vindo ao seu Menu de Login")
    print("------------------------------")

    u = input("User: ")
    s = int(input("Senha: "))
    if u == usuario and s == senha:
        user_login = True 
    else:
        user_login = False

    if user_login == True:
        print("Você foi loggado com sucesso!")
    else:
        print("Nome de Usuário ou Senha incorretos, tente outra vez!")

if __name__ == "__main__":
    main()