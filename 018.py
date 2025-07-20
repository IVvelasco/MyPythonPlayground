# Level 018

#  --------------------------
#  -- ÁREA DE UM RETÂNGULO --
#  --------------------------

print("Vamos calcular a área de um retângulo!")
base = float(input("Coloque aqui o tamanho da base: "))
altura = float(input("Insira a altura: "))
area = base * altura 

if base == altura:
    print(f"Hey, isso é um quadrado! Área: {area}")
else:
    print(f"A àrea total do retângulo é:{area}")
