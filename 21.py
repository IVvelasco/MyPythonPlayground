# Level 021

# -----------------------------------
# -- FAIXA ETÁRIA COM IF-ELIF-ELSE --
# -----------------------------------

idade = int(input("Por favor, insira a sua idade (Utilize apenas números inteiros): "))

if idade <= 12:
    print("Segundo a classificação oficial brasileira, sua faixa etária é: Criança!")
elif idade <=19:
    print("Segundo a classificação oficial brasileira, sua faixa etária é: Adolescente")
elif idade <= 59:
    print("Segundo a classificação oficial brasileira, sua faixa etária é: Adulto!")
else: 
    print("Segundo a classificação oficial brasileira, sua faixa etária é: Idoso!")