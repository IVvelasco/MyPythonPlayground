# Level 032

#  -----------------------------
#  -- TENTANDO COM def main() --
#  -----------------------------

def main():
    print("*****************************************************")
    print("*     TESTE PARA DESCOBRIR SE VOCÊ É UM VAMPIRO     *")
    print("*****************************************************")

    probabilidade = int(0)
    mordida = input("Você foi mordido recentemente por um vampiro? [s/n] ")
    if mordida == 's':
        probabilidade += 1 
    elif mordida == 'n':
        probabilidade += 0
    else:
        print("Insira uma resposta válida!")

    idade = int(input("Sua idade: "))
    if idade >= 100:
        probabilidade += 1
    elif idade <=100:
        probabilidade += 0 
    else:
        print("Insira uma resposta válida!")

    alho = input("Você tem medo de alho: [s/n] ")
    if alho == 's':
        probabilidade += 1 
    elif alho == 'n':
        probabilidade += 0
    else:
        print("Insira uma resposta válida!")

    mora = input("Você mora em um castelo medieval? [s/n] ")
    if mora == 's':
        probabilidade += 1 
    elif mora == 'n':
        probabilidade += 0
    else:
        print("Insira uma resposta válida!")

    crucifixo = input("Você sente desconforto perto de crucifixos? [s/n] ")
    if crucifixo == 's':
        probabilidade += 1 
    elif crucifixo == 'n':
        probabilidade += 0
    else:
        print("Insira uma resposta válida")

    sol = input("Você evita o sol? [s/n] ")
    if sol == 's':
        probabilidade += 1
    elif sol == 'n':
        probabilidade += 0
    else:
        print("Insira uma resposta válida!")

    igreja = input("Você evita ir a Igrejas? [s/n] ")
    if igreja == 's':
        probabilidade += 1
    elif igreja == 'n':
        probabilidade += 0
    else:
        print("Insira uma resposta válida!")

    sangue = input("Quando vê sangue você sente água na boca? [s/n] ")
    if sangue == 's':
        probabilidade += 1 
    elif sangue == 'n':
        probabilidade += 0 
    else: 
        print("Insira uma resposta válida!")

    if probabilidade >= 5:
        print("VAMPIRO!!!")
    else:
        print("Você é só emo mesmo")
if __name__ == "__main__":
    main()
