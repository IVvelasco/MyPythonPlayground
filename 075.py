# Level 075

# ----------------------
# -- BARALHO ESPANHOL --
# ----------------------

print('*' * 70)
print('Você sabia que o baralho espanhol tem naipes divididos de acordo com a hierarquia social?')
print('*' * 70)
print("Vamos comparar as cartas do baralho tradicional com o baralho espanhol e ver a diferença dos naipes!")
print('*' * 70)
print("ESPADAS = E")
print('*' * 70)
print("COPAS = C")
print('*' * 70)
print("OUROS = O")
print('*' * 70)
print("PAUS = P")
print('*' * 70)

carta = input('Insira uma letra e verifique o Naipe: ')

if carta == 'E':
    print("Espadas(Espada): Representa o poder militar e a nobreza")
elif carta == 'C':
    print("Copas(Cáliz): Simboliza a religião e o clero.")
elif carta == 'O':
    print("Ouros (Denário): Representa a riqueza, o comércio e os banqueiros.")
elif carta == 'P':
    print("Bastos(Basto): Simboliza os trabalhadores rurais e os camponeses.")
else:
    print("Insira um naipe válido!")