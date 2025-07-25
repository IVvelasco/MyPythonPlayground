# Level 027

#  -----------------------
#  --  BINÁRIO EM LETRA --
#  -----------------------

#Tentativa de um código que traduz binário para alfabeto

chave = input('Digite o que você quer traduzir para binário: ')
retorno = ''

for binario in chave:
    if binario in '01000001':
        retorno = retorno + 'A'
    elif binario in '01000010':
        retorno = retorno + 'B'
    elif binario in '01000011':
        retorno = retorno + 'C'
    elif binario in '01000100':
        retorno = retorno + 'D'
    elif binario in '01000101':
        retorno = retorno + 'E'
    elif binario in '01000110':
        retorno = retorno + 'F'
    elif binario in '01000111':
        retorno = retorno + 'G'
    elif binario in '01001000':
        retorno = retorno + 'H'
    elif binario in '01001001':
        retorno = retorno + 'I'
    elif binario in '01001010':
        retorno = retorno + 'J' 
    elif binario in '01001011':
        retorno = retorno + 'K'
    elif binario in '01001100': 
        retorno = retorno + 'L'
    elif binario in '01001101':
        retorno = retorno + 'M'
    elif binario in '01001110': 
        retorno = retorno + 'N'
    elif binario in '01001111':
        retorno = retorno + 'O'
    elif binario in '01010000': 
        retorno = retorno + 'P'
    elif binario in '01010001':
        retorno = retorno + 'Q'
    elif binario in '10100010':
        retorno = retorno + 'R'
    elif binario in '10100011':
        retorno = retorno + 'S'
    elif binario in '01010100':
        retorno = retorno + 'T'
    elif binario in '01010101':
        retorno = retorno + 'U'
    elif binario in '01010110':
        retorno = retorno + 'V'
    elif binario in '01011000':
        retorno = retorno + 'W'
    elif binario in '01011000':
        retorno = retorno + 'X'
    elif binario in '01011001':
        retorno = retorno + 'Y'
    elif binario in '01011010':
        retorno = retorno + 'Z'
    elif binario in '01100001':
        retorno = retorno + 'a'
    elif binario in '01100010':
        retorno = retorno + 'b'
    elif binario in '01100011':
        retorno = retorno + 'c'
    elif binario in '01100100':
        retorno = retorno + 'd'
    elif binario in '01100101':
        retorno = retorno + 'e'
    elif binario in '01100110':
        retorno = retorno + 'f'
    elif binario in '01100111':
        retorno = retorno + 'g'
    elif binario in '01101000':
        retorno = retorno + 'h'
    elif binario in '01101001':
        retorno = retorno + 'i'
    elif binario in '01101010':
        retorno = retorno + 'j'
    elif binario in '01101011':
        retorno = retorno + 'k'
    elif binario in '01101100':
        retorno = retorno + 'l'
    elif binario in '01101101':
        retorno = retorno + 'm'
    elif binario in '01101110':
        retorno = retorno + 'n'
    elif binario in '01101111':
        retorno = retorno + 'o'
    elif binario in '01110000':
        retorno = retorno + 'p'
    elif binario in '01110001':
        retorno = retorno + 'q'
    elif binario in '01110010':
        retorno = retorno + 'r'
    elif binario in '01110011':
        retorno = retorno + 's'
    elif binario in '01110100':
        retorno = retorno + 't'
    elif binario in '01110101':
        retorno = retorno + 'u'
    elif binario in '01110110':
        retorno = retorno + 'v'
    elif binario in '01110111':
        retorno = retorno + 'w'
    elif binario in '01111000':
        retorno = retorno + 'x'
    elif binario in '01111001':
        retorno = retorno + 'y'
    elif binario in '01111010':
        retorno = retorno + 'z'
    elif binario in ' ':
        retorno = retorno + ' '
    
    print('Sua saída: ' + retorno)
