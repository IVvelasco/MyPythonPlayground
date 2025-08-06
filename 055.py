# Level 055

# -----------------------------------
# -- 30% DE DESCONTO EM UMA COMPRA --
# -----------------------------------

"""
Adaptado do Visualg para Python, com base nos exercícios práticos da UltraCursos
"""


liquidificador = float(1500)
fogao = float(4000)
aspirador = float(1500)


print("------------------------------------------------------------------------")
print("Você vai receber 30% de desconto na compra de qualquer um desses itens: ")
print("------------------------------------------------------------------------")
print("1) Liquidificador R$1500.00")
print("------------------------------------------------------------------------")
print("2) Fogão 4 bocas R$4000")
print("------------------------------------------------------------------------")
print("3) Aspirador de pó R$1500")
print("------------------------------------------------------------------------")
escolha = int(input("Qual dos itens você prefere?R: "))

if escolha == 1:
    desconto = liquidificador * 30 / 100
    print(f"Seu desconto será: R${desconto :.2f}")
    total = liquidificador - desconto
    print(f"Total a pagar: R${total :.2f}")
elif escolha == 2:
    desconto = fogao * 30 / 100
    print(f"Seu desconto será de: R${desconto :.2f}")
    total = fogao - desconto
    print(f"Total a pagar: R${total :.2f}")
elif escolha == 3:
    desconto = aspirador * 30 / 100
    print(f"Seu desconto será: R${desconto :.2f}")
    total = aspirador - desconto
    print(f"Total a pagar: R${total :.2f}")
else:
    print("Insira um dado válido!")