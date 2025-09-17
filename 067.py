# Level 067

# -----------
# -- BUSÃO --
# -----------

passagem = float("4.30")
meia_passagem = passagem / 2
idoso = input("Você é idoso? [S/n]: ")
if idoso == 'S':
        print("Você não precisa pagar pela passagem")
else:
    estudante = input("Você é estudante? [S/n]: ")
    if estudante == 'S':
            credito = float(input("Quanto você tem no seu VEM?R: "))
            if credito < meia_passagem:
                 print("Você não tem crédito para essa viagem")
            else:
                credito = credito - meia_passagem
                print(f"O valor da sua passagem é R${meia_passagem} e o crédito restante é de R${credito:.2}")
    elif estudante == 'n':
        credito = float(input("Quanto você tem no seu VEM?R: "))
        if credito < passagem:
            print("Você não tem crédito para entrar no ônibus")
        else: 
            credito = credito - passagem
            print(f"O valor da sua passagem é: R${passagem} e o crédito restante é R${credito:.2}")