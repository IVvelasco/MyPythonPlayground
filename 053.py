# Level 053

# ---------------------------------
# -- 10% DO GARÇOM EM PYPIZZARIA --
# ---------------------------------

def menu():
    
    print("=============================================")
    print("====================MENU=====================")
    print("---------------------------------------------")
    print("Rodízio por pessoa R$29,99 🍕") 
    print("---------------------------------------------")
    print("Coca-cola R$4,99 🥤")
    print("---------------------------------------------")
    print("Pizza Inteira R$99.99 🍕🍕")
    print("=============================================")

def bill_calculator():
   
    rodizio = 29.99
    coca = 4.99
    pizza = 99.99
    
    rodizio_request = int(input("Quantos adultos vão querer rodízio? R: "))
    meio_request = int(input("Quantas crianças vão participar? Até os 12 paga só metade! R: "))
    coca_request = int(input("Quantos litrões de coca-cola foram pedidos? R: "))
    pizza_request = int(input("Quantas pizzas foram pedidas? R: "))
    
    
    rodizio_total =  rodizio * rodizio_request
    meio_total = rodizio / 2
    rodizio_t = rodizio_total + meio_total
    coca_total = coca * coca_request
    pizza_total = pizza * pizza_request
    
    total = rodizio_total + meio_total + coca_total + pizza_total
    garcom = total / 10 
    total_total = total + garcom
    
    amigos = int(input("Quantas pessoas (incluindo você) vão pagar a conta?? R: "))
    conta_dividida = total_total / amigos
    
    print(f"\n🍕 Conta:")
    print(f"Rodízio: R${rodizio} x {rodizio_request:.2f} & {meio_request} x R${meio_total:.2f}= R${rodizio_t:.2f}")
    print(f"Coca-Cola: R${coca} x {coca_request:.2f} = R${coca_total:.2f}")
    print(f"Pizza Inteira: R${pizza} x {pizza_request:.2f} = R${pizza_total:.2f}")
    print(f"Porcentagem do garçom: R${garcom:.2f}")
    print(f"─" * 50)
    print(f"💰 Total: R${total_total:.2f}")
    print(f"👥 Dividido por {amigos} pessoas: R${conta_dividida:.2f} para cada um")
    print(f"Saúde! 🍻")

def main():
    print("🍕 Bem-vindo a pyPizzaria! 🍕\n")
    menu()
    print()
    bill_calculator()

if __name__ == "__main__":
    main()