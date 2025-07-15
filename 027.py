
# Level 027

#  -----------------------
#  -- Letra em Binário  --
#  -----------------------

#Tentativa de um código que traduz alfabeto para binário

chave = input('Digite o que você quer traduzir para binário: ')
retorno = ''

for letra in chave:
    if letra in 'A':
        retorno = retorno + '01000001 '
    elif letra in 'B':
        retorno = retorno + '01000010 '
    elif letra in 'C':
        retorno = retorno + '01000011 '
    elif letra in 'D':
        retorno = retorno + '01000100 '
    elif letra in 'E':
        retorno = retorno + '01000101 '
    elif letra in 'F':
        retorno = retorno + '01000110 '
    elif letra in 'G':
        retorno = retorno + '01000111 '
    elif letra in 'H':
        retorno = retorno + '01001000 '
    elif letra in 'I':
        retorno = retorno + '01001001 '
    elif letra in 'J':
        retorno = retorno + '01001010 ' 
    elif letra in 'K':
        retorno = retorno + '01001011 '
    elif letra in 'L': 
        retorno = retorno + '01001100 '
    elif letra in 'M':
        retorno = retorno + '01001101 '
    elif letra in 'N': 
        retorno = retorno + '01001110 '
    elif letra in 'O':
        retorno = retorno + '01001111 '
    elif letra in 'P': 
        retorno = retorno + '01010000 '
    elif letra in 'Q':
        retorno = retorno + '01010001 '
    elif letra in 'R':
        retorno = retorno + '10100010 '
    elif letra in 'S':
        retorno = retorno + '10100011 '
    elif letra in 'T':
        retorno = retorno + '01010100 '
    elif letra in 'U':
        retorno = retorno + '01010101 '
    elif letra in 'V':
        retorno = retorno + '01010110 '
    elif letra in 'W':
        retorno = retorno + '01010111 '
    elif letra in 'X':
        retorno = retorno + '01011000 '
    elif letra in 'Y':
        retorno = retorno + '01011001 '
    elif letra in 'Z':
        retorno = retorno + '01011010 '
    elif letra in 'a':
        retorno = retorno + '01100001 '
    elif letra in 'b':
        retorno = retorno + '01100010 '
    elif letra in 'c':
        retorno = retorno + '01100011 '
    elif letra in 'd':
        retorno = retorno + '01100100 '
    elif letra in 'e':
        retorno = retorno + '01100101 '
    elif letra in 'f':
        retorno = retorno + '01100110 '
    elif letra in 'g':
        retorno = retorno + '01100111 '
    elif letra in 'h':
        retorno = retorno + '01101000 '
    elif letra in 'i':
        retorno = retorno + '01101001 '
    elif letra in 'j':
        retorno = retorno + '01101010 '
    elif letra in 'k':
        retorno = retorno + '01101011 '
    elif letra in 'l':
        retorno = retorno + '01101100 '
    elif letra in 'm':
        retorno = retorno + '01101101 '
    elif letra in 'n':
        retorno = retorno + '01101110 '
    elif letra in 'o':
        retorno = retorno + '01101111 '
    elif letra in 'p':
        retorno = retorno + '01110000 '
    elif letra in 'q':
        retorno = retorno + '01110001 '
    elif letra in 'r':
        retorno = retorno + '01110010 '
    elif letra in 's':
        retorno = retorno + '01110011 '
    elif letra in 't':
        retorno = retorno + '01110100 '
    elif letra in 'u':
        retorno = retorno + '01110101 '
    elif letra in 'v':
        retorno = retorno + '01110110 '
    elif letra in 'w':
        retorno = retorno + '01110111 '
    elif letra in 'x':
        retorno = retorno + '01111000 '
    elif letra in 'y':
        retorno = retorno + '01111001 '
    elif letra in 'z':
        retorno = retorno + '01111010 '
    
    print('Sua saída: ' + retorno)