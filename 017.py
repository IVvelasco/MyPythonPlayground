# Level 017

#  -------------------
#  -- PIZZA & INPUT --
#  -------------------

print("##############################################")
print("# Bem-Vindo a Pypizza, qual seu pedido hoje? #")
print("##############################################")



pizza = int(input("Insira aqui a quantidade de pizzas: "))
valor_pizza = float(19.99)
total0 = valor_pizza * pizza

refrigerante = int(input("Insira aqui a quantidade de refrigerantes: "))
valor_refri = float(4.99)
total1 = valor_refri * refrigerante

print(f"O total a pagar é R${total0 + total1:.2f}") # Esse :.2f limita as casas decimais que serão exibidas na tela