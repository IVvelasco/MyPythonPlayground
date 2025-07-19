# Level 040

#  -----------------------------
#  -- CRIPTOGRAFIA COM RANDOM --
#  -----------------------------

#Tentativa de um código que traduz alfabeto para binário

import random 

def main(): 

    chave = input('Digite a palavra que você quer criptografar: ')
    retorno = '' 
    letra1 = [
        "A", "B","C", "D",  "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
        ]
    
    for letra in chave:
        if letra in 'A':
            retorno = retorno + random.choice(letra1)
            retorno = retorno + random.choice(letra1) 
        elif letra in 'C':
            retorno = retorno + random.choice(letra1) 
        elif letra in 'D':
            retorno = retorno + random.choice(letra1) 
        elif letra in 'E':
            retorno = retorno + random.choice(letra1) 
        elif letra in 'F':
            retorno = retorno + random.choice(letra1) 
        elif letra in 'G':
            retorno = retorno + random.choice(letra1) 
        elif letra in 'H':
            retorno = retorno + random.choice(letra1)
        elif letra in 'I':
            retorno = retorno + random.choice(letra1) 
        elif letra in 'J':
            retorno = retorno + random.choice(letra1) 
        elif letra in 'K':
            retorno = retorno + random.choice(letra1) 
        elif letra in 'L': 
            retorno = retorno + random.choice(letra1) 
        elif letra in 'M':
            retorno = retorno + random.choice(letra1) 
        elif letra in 'N': 
            retorno = retorno + random.choice(letra1)
        elif letra in 'O':
            retorno = retorno + random.choice(letra1) 
        elif letra in 'P': 
            retorno = retorno + random.choice(letra1) 
        elif letra in 'Q':
            retorno = retorno + random.choice(letra1) 
        elif letra in 'R':
            retorno = retorno + random.choice(letra1) 
        elif letra in 'S':
            retorno = retorno + random.choice(letra1) 
        elif letra in 'T':
            retorno = retorno + random.choice(letra1) 
        elif letra in 'U':
            retorno = retorno + random.choice(letra1) 
        elif letra in 'V':
            retorno = retorno + random.choice(letra1) 
        elif letra in 'W':
            retorno = retorno + random.choice(letra1) 
        elif letra in 'X':
            retorno = retorno + random.choice(letra1)  
        elif letra in 'Y':
            retorno = retorno + random.choice(letra1)  
        elif letra in 'Z':
            retorno = retorno + random.choice(letra1)  
        elif letra in 'a':
            retorno = retorno + random.choice(letra1)  
        elif letra in 'b':
            retorno = retorno + random.choice(letra1)  
        elif letra in 'c':
            retorno = retorno + random.choice(letra1) 
        elif letra in 'd':
            retorno = retorno + random.choice(letra1) 
        elif letra in 'e':
            retorno = retorno + random.choice(letra1) 
        elif letra in 'f':
            retorno = retorno + random.choice(letra1) 
        elif letra in 'g':
            retorno = retorno + random.choice(letra1)  
        elif letra in 'h':
            retorno = retorno + random.choice(letra1)  
        elif letra in 'i':
            retorno = retorno + random.choice(letra1)  
        elif letra in 'j':
            retorno = retorno + random.choice(letra1)  
        elif letra in 'k':
            retorno = retorno + random.choice(letra1) 
        elif letra in 'l':
            retorno = retorno + random.choice(letra1) 
        elif letra in 'm':
            retorno = retorno + random.choice(letra1) 
        elif letra in 'n':
            retorno = retorno + random.choice(letra1) 
        elif letra in 'o':
            retorno = retorno + random.choice(letra1) 
        elif letra in 'p':
            retorno = retorno + random.choice(letra1) 
        elif letra in 'q':
            retorno = retorno + random.choice(letra1)
        elif letra in 'r':
            retorno = retorno + random.choice(letra1) 
        elif letra in 's':
            retorno = retorno + random.choice(letra1) 
        elif letra in 't':
            retorno = retorno + random.choice(letra1) 
        elif letra in 'u':
            retorno = retorno + random.choice(letra1) 
        elif letra in 'v':
            retorno = retorno + random.choice(letra1) 
        elif letra in 'w':
            retorno = retorno + random.choice(letra1)  
        elif letra in 'x':
            retorno = retorno + random.choice(letra1)  
        elif letra in 'y':
            retorno = retorno + random.choice(letra1) 
        elif letra in 'z':
            retorno = retorno + random.choice(letra1)
    
        print(f'Resultado da criptografia: {retorno}')

if __name__ == '__main__':
    main()