# Level 060

# -----------------------------------
# -- CÁLCULO DA PENSÃO ALIMENTÍCIA -- 
# -----------------------------------

salario = float(input("Insina aqui seu salário líquido: "))
porcentagem = float(input("Insira a porcentagem fixada pelo juiz: "))
pensao = salario * porcentagem / 100 
print(f"O valor de pensão a ser pago é de R${pensao :.2f}")

