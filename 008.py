# Level 008

# ---------------------------
# -- Brincando com strings --
# ---------------------------


"""
Uma maneira simples e eficiente de testar se uma frase ou palavra trata-se de um palíndromo: comparar a string ::+1 com ::-1 e ver se são correspondentes

"""

frase = input("Será um palíndromo? Digite e descubra: ")

if frase == frase [::-1]:
    print(f"Uau, é um palindromo!")
else:
    print(f"Não foi dessa vez!")
