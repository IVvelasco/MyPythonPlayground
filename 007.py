# Level 007

# --------------
# -- CONVERSOR --
# --------------


def converter_dias(dias):
    """
    Converte dias em horas, minutos e segundos
    """

    horas = dias * 24
    minutos = horas * 60
    segundos = minutos * 60

    return horas, minutos, segundos

def main ():
    print("=== CONVERSOR DE DIAS ===")

    try: 
        # Solicita o nuḿero de dias ao usuário
        dias = float(input("Digite o número de dias: "))

        # Calcula as conversões
        horas, minutos, segundos = converter_dias(dias)

        # Exibe os resultados 
        print(f"\nOs seus {dias} dias de rabo ardido equivalem a: ")
        print(f"{horas:,.0f} horas")
        print(f"{minutos:,.0f} minutos")
        print(f"{segundos:,.0f} segundos")

    except ValueError:
        print("Erro, por favor insira um número válido, humano!")

if __name__ == "__main__":
    main()
