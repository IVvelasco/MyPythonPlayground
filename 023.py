# Level 022

# ------------------------------
# -- Interação com o usuáriro --
# ------------------------------

nome = input("Insira aqui seu nome: ")
sobrenome = input("Insira aqui seu sobrenome: ")
idade = int(input("Insira aqui sua idade: "))
comida = input("Insira aqui sua comida favorita: ")
cor = input("Insira aqui sua cor favorita: ")
hobbies = input("Insira aqui seus hobbies: ")
animal = input("Você possui animais de estimação? [s/n]: ")
if animal == 's':
    animal = "Você possui animal de estimação"
else:
    animal ="Você não possui animais de estimação"

print(f"Olá {nome} {sobrenome}, sua idade é {idade}, sua comida favorita é {comida}, seu(s) hobbies são: {hobbies}. Sobre animais de estimação: {animal} ")
