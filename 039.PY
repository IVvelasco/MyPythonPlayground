# LEVEL 039

# ----------------------
# -- AGRUPANDO ALUNOS --
# ----------------------

def main():
        alunos = int(input("Quantos alunos você pretende agrupar? R: "))
        agrupamento = int(input("Quantos alunos por grupo? R: "))
        grupos = alunos // agrupamento
        sobra = alunos % agrupamento
        print(f"Você tem {grupos:.0f} grupos de alunos, com uma sobra de {sobra:.0f}")

if __name__ == "__main__":
    main()