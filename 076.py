# Level 076

# ------------
# -- XADREZ --
# ------------


print('#' * 50)
print("Bora descobrir um pouco mais sobre mim? Sua missão é descobrir minha jogada favorita no xadrez. ")
print('#' * 50)

questao = input("Minha jogada faz parte da abertura? S/N: ")
if questao == 'N':
    print("Errou, tente outra vez!")
elif 'S':
    print('Você passou para a próxima etapa')
    questao2 = input("Minha jogada é com as pretas ou as brancas?R: ")
    if questao2 == 'brancas':
        print("Você errou, tente de novo")
    elif 'pretas':
        print("Você está indo super bem, vamos prosseguir")
        print("#" * 50)
        print("TORRES(T), CAVALOS(C), BISPO(B), RAINHA(RA), REI(R)")
        print("#" * 50)
        questao3 = input("Hora de testar sua sorte, tente adivinhar com quais peças eu executo essa jogada: ")
        if questao3 == 'T':
            print("Tente outra vez!")
        elif questao3 == 'B':
            print("Tente outra vez!")
        elif questao3 == 'RH':
            print("Tente outra vez!")
        elif questao3 == 'R':
            print("Tente outra vez!")
        elif questao3 == 'C':
            print("Parabéns, você avançou para a próxima!")
            print("Hora de revelar, minha jogada favorita: DEFESA PRUSSINA ouu abertura de dois cavalos, um tipo de defesa ofensiva utilizada pelas peças pretas")
            