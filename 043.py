# LEVEL 043

# --------------------
# -- FRASES DE AMOR --
# --------------------


def main ():

    print("10 Frases Aleatórias para declarar seu amor") 
    poema0 = "Ganho meu dia quando recebo suas notificações." 
    poema1 = "Roubo seu tempo para te adorar." 
    poema2 = "Ironicamente, minha vida só ficou arrumada quando você a virou de cabeça para baixo." 
    poema3 = "Nada me fará deixar de amar-te, a lua é minha testemunha." 
    poema4 = "Goste ou não, somos nós dois até o fim." 
    poema5 = "Os dias vem e vão, meu amor permanece." 
    poema6 = "Você ilumina meus dias." 
    poema7 = "Amar você é a melhor parte da minha vida." 
    poema8 = "Amar é ter a certeza de que, aconteça o que acontecer, nunca estaremos sozinhos." 
    poema9 =  "Você é o meu refúgio." 

    poema = int(input("Escolha um número de 0 a 9: "))
    if poema == 0:
        print(f"Seu poema é: {poema0}")
    elif poema == 1: 
        print(f"Seu poema é: {poema1}")
    elif poema == 2: 
        print(f"Seu poema é: {poema2}")
    elif poema == 3: 
        print(f"Seu poema é: {poema3}")
    elif poema == 4: 
        print(f"Seu poema é: {poema4}")
    elif poema == 5: 
        print(f"Seu poema é: {poema5}")
    elif poema == 6: 
        print(f"Seu poema é: {poema6}")
    elif poema == 7: 
        print(f"Seu poema é: {poema7}")
    elif poema == 8: 
        print(f"Seu poema é: {poema8}")
    elif poema == 9: 
        print(f"Seu poema é: {poema9}")
    else:
        print("Escolha um valor válido!")

if __name__ == '__main__':
    main()