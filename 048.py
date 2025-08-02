# Level 048

# ------------------------------
# -- QUESTIONÁRIO COM LOOPING --
# ------------------------------

print("Qual a minha trilogia favorita de filmes?")
print("a) Matrix")  
print("b) Jogos Vorazes")
print("c) Crepúsculo")

palpite = input("R: ")

while palpite != 'a':
    print("Você errou!")
    palpite = input("Tente de novo: ")
else:
    print("Parabéns, você acertou!")    
