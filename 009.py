# Level 009 

# --------------------------------
# -- Usando escolhas aleatórias --
# --------------------------------

import random
numero = random.randint(1, 1000)
palpite = int(input("Escolha um número aleatório entre 1 e 1000: "))

if numero == palpite:
    print("Parabéns, suas chances eram mínimas mas você conseguiu!")
else:
    print(f"A resposta era: ", numero)
    print("Não desista, tente outra vez!")