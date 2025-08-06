# Level 057

# ------------------------------
# -- MAIOR OU MENOR (NÚMEROS) --
# ------------------------------

""" 
Adaptado do Visualg para Python, com base nos exercícios práticos da UltraCursos
"""

A = float(input("Insira o primeiro número: "))
B = float(input("Insira o segundo número: "))
if A > B:
    print(f"{A} é maior que {B}!")
elif A < B:
    print(f"{A} é menor que {B}!")
elif A == B:
    print(f"{A} é igual a {B}!")
else:
    print("Por favor, insira um valor válido.")
