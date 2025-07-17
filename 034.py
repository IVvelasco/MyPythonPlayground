# Level 033
# ----------------------------------
# -- RACHANDO A CONTA DO BOTECO 2 --
# ----------------------------------

def menu():
    """Função que mostra o menu do boteco"""
    print("=============================================")
    print("====================MENU====================")
    print("---------------------------------------------")
    print("Cerveja R$5.99")
    print("---------------------------------------------")
    print("Petisco R$9.99")
    print("---------------------------------------------")
    print("Porção R$19.99")
    print("=============================================")

def calcular_conta():
   
    valor_cerveja = 5.99
    valor_petisco = 9.99
    valor_porcao = 19.99
    
    pedido_cerveja = int(input("Quantas cervejas você pediu? R: "))
    pedido_petisco = int(input("Quantos petiscos foram pedidos? R: "))
    pedido_porcao = int(input("Quantas porções foram pedidas? R: "))
    
    
    conta_cerveja = valor_cerveja * pedido_cerveja
    conta_petisco = valor_petisco * pedido_petisco
    conta_porcao = valor_porcao * pedido_porcao
    
    total = conta_cerveja + conta_petisco + conta_porcao
    
    pessoas = int(input("Com quantas pessoas (incluindo você) vai dividir? R: "))
    valor_por_pessoa = total / pessoas
    
    print(f"\n🍺 Resumo da conta:")
    print(f"Cervejas: {pedido_cerveja} x R${valor_cerveja:.2f} = R${conta_cerveja:.2f}")
    print(f"Petiscos: {pedido_petisco} x R${valor_petisco:.2f} = R${conta_petisco:.2f}")
    print(f"Porções: {pedido_porcao} x R${valor_porcao:.2f} = R${conta_porcao:.2f}")
    print(f"─" * 50)
    print(f"💰 Total: R${total:.2f}")
    print(f"👥 Dividindo por {pessoas} pessoas: R${valor_por_pessoa:.2f} cada um")
    print(f"Saúde! 🍻")

def main():
    """Função principal que coordena tudo"""
    print("🍺 Bem-vindo ao Buteco.py! 🍺\n")
    menu()
    print()
    calcular_conta()

if __name__ == "__main__":
    main()