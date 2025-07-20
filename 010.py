# Level 010

# ------------------------
# -- ADIVINHE O NÚMERO --
# ------------------------

import random

numero = random.randint(1, 1000)
acertou = False

while not acertou:
    palpite = int(input("Escolha um número aleatório entre 1 e 1000: "))

    if numero == palpite:
        print("Parabéns, suas chances eram mínimas mas você conseguiu!")
        acertou = True
    else: 
        print("Não desista, tente outra vez!")

    # Bônus para o jogador

        if palpite < numero:
            print("Tente um número maior!")
        else: 
            print("Tente um número menor")
