# Level 010

# ----------------------------
# -- CALCULADORA INTERATIVA --
# ----------------------------

print("Coloque dois números e escolha um dos operadores básicos: ")
print("(+) --> Adição") 
print("(-) --> Subtração")
print("(/) Divisão")
print("(*) Multiplicação")

n1 = int(input("Escolha o primeiro número: "))
n2 = int(input("Escolha o segundo número: ")) 
operador = input('Escolha o operador: ') 

if operador == '+':
    resultado = (n1 + n2)
elif operador == '-':
    resultado = (n1 - n2)
elif operador == '/':
    resulado = (n1 / n2)
elif operador == '*':
    resultado = (n1 * n2)


print(f"resultado = {resultado}")
