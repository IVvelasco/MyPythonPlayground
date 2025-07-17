# Level 033

#  --------------------------------
#  -- RACHANDO A CONTA DO BOTECO --
#  --------------------------------

def main():
    valor = float(input("Qual é o valor total da conta? "))
    amigos = int(input("Quantos amigos vão rachar a conta com você? "))
    rachando = valor / amigos 
    print(f"Ficou R${rachando:.2f} para cada um.")

if __name__ == main():
    main()
