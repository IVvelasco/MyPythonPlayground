# Level 022

# ---------------------------------------
# -- Fillmes: Classificação Indicativa --
# ---------------------------------------

idade = int(input("Por favor, insira a sua idade(Utilize apenas números inteiros) e descubra sua classificação indicativa: "))

if idade <= 9:
    print("--------------------------------------------------------------------------------------------")
    print("Segundo a classificação indicativa brasileira, sua faixa para filmes é: CLASSIFICAÇÃO LIVRE")
    print("--------------------------------------------------------------------------------------------")
    print("--------------------------------------------------------------------------------------------")
    print("Essa classificação não expõe a criança a conteúdos potencialmente prejudiciais")
    print("--------------------------------------------------------------------------------------------")
elif idade <=10:
    print("----------------------------------------------------------------------------------------------------------")
    print("Segundo a classificação indicativa brasileira, sua faixa para filmes é: PROIBIDO PARA MENORES DE 10 ANOS")
    print("----------------------------------------------------------------------------------------------------------")
    print("----------------------------------------------------------------------------------------------------------")
    print("O filme pode ter conteúdo violento ou linguagem inapropriada para crianças, ainda que em menor intensidade")
    print("----------------------------------------------------------------------------------------------------------")
elif idade <=11:
    print("--------------------------------------------------------------------------------------------------------")
    print("Segundo a classificação indicativa brasileira, sua faixa para filmes é: PROIBIDO PARA MENORES DE 12 ANOS")
    print("--------------------------------------------------------------------------------------------------------")
    print("--------------------------------------------------------------------------------------------------------")
    print("As cenas podem conter agressão física, consumo de drogas e insinuação sexual")
    print("--------------------------------------------------------------------------------------------------------")
elif idade <=13:
    print("--------------------------------------------------------------------------------------------------------")
    print("Segundo a classificação indicativa brasileira, sua faixa para filmes é: PROIBIDO PARA MENORES DE 14 ANOS")
    print("--------------------------------------------------------------------------------------------------------")
    print("--------------------------------------------------------------------------------------------------------")
    print("Conteúdo mais violento e/ou de linguagem sexual mais acentuada")
    print("--------------------------------------------------------------------------------------------------------")
elif idade <=15:
    print("------------------------------------------------------------------------------------------------------------------")
    print("Segundo a classificação indicativa brasileira, sua faixa para filmes é: PROIBIDO PARA MENORES DE 16 ANOS")
    print("------------------------------------------------------------------------------------------------------------------")
    print("------------------------------------------------------------------------------------------------------------------")
    print("Conteúdo mais violento ou com conteúdo visual mais intenso, com cenas de tortura, suicídio, estupro ou nudez total")
    print("------------------------------------------------------------------------------------------------------------------") 
elif idade <=17:
    print("--------------------------------------------------------------------------------------------------------------------------")
    print("Segundo a classificação indicativa brasileira, sua faixa para filmes é: PROIBIDO PARA MENORES DE 18 ANOS")
    print("--------------------------------------------------------------------------------------------------------------------------") 
    print("--------------------------------------------------------------------------------------------------------------------------")
    print("Conteúdos violentos e sexuais extremos. Com cenas de sexo, incesto ou atos repetidos de tortura, mutilação ou abuso sexual")
    print("--------------------------------------------------------------------------------------------------------------------------")
elif idade >=18:
    print("Maior de 18 pode assistir ao filme que quiser ;) ")
