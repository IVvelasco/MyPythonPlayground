# Level 056 

# --------------------------------
# -- VOLUME DE UMA LATA DE ÓLEO --
# --------------------------------

""" 
Adaptado do Visualg para Python, com base nos exercícios práticos da UltraCursos
"""

print("-" * 58)
print("-- VAMOS CÁLCULAR O VALOR DO VOLUME DE UMA LATA DE ÓLEO --")
print("-" * 58)

v = float(3.14159)
a = float(input("Insira a altura: "))
r = float(input("Insira o raio: "))
resultado = (r*2) * v * a 

print(f"O volume da lata de óleo é: {resultado :.2f} ml")