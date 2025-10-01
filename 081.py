# Level 080

# -----------------
# -- BUBBLE SORT --
# --  INVERTIDO  --
# -----------------

"Algoritmo de Bubble Sort feito durante uma call de transmissão do Discord, "
"Orientador: Andreas Colavite"

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] < lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

numeros = [3,57,1,5,2,4,6,2,1,4,2,3,46,13,0]
print("Lista original: ", numeros)
print("Lista ordenada: ", bubble_sort(numeros))