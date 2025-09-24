# Level 079

# ------------------------
# -- ESPÉCIES DE PYTHON --
# ------------------------

class Python:
    def __init__(self, especie, nome_popular, genero, descoberta, local):
        self.especie = especie
        self.nome_popular = nome_popular
        self.genero = genero
        self.descoberta = descoberta
        self.local = local

    def __str__(self):
        return f"Espécie: {self.especie}, Nome Popular: {self.nome_popular}, Gênero: {self.genero}, Ano de Descoberta: {self.descoberta}, Locais onde é encontrada: {self.local}"
    
class Catalogo:
    def __init__(self):
        self.python = []

    def adicionar_python(self, python):
        self.python.append(python)

    def pesquisar_por_especie(self, especie_pesquisa):
        especies_encontradas = []
        for python in self.python:
            if especie_pesquisa.lower() in python.especie.lower():
                especies_encontradas.append(python)
        return especies_encontradas
    
    def pesquisar_por_nome_popular(self, nome_popular_pesquisa):
        especies_encontradas = []
        for python in self.python:
            if nome_popular_pesquisa.lower() in python.nome_popular.lower():
                especies_encontradas.append(python)
        return especies_encontradas  
    
    def pesquisar_por_genero(self, genero_pesquisa):
        especies_encontradas = []
        for python in self.python:
            if genero_pesquisa.lower() in python.genero.lower():
                especies_encontradas.append(python)
        return especies_encontradas  
        
    def pesquisar_por_descoberta(self, descoberta_pesquisa):
        especies_encontradas = []
        for python in self.python:
            if descoberta_pesquisa.lower() in python.descoberta.lower():
                especies_encontradas.append(python)
        return especies_encontradas  
    
    def pesquisar_por_local(self, descoberta_local):
        especies_encontradas = []
        for python in self.python:
            if descoberta_local.lower() in python.local.lower():
                especies_encontradas.append(python)
        return especies_encontradas  
        
    def pesquisar_geral(self, termo_pesquisa):
        especies_encontradas = []
        termo_lower = termo_pesquisa.lower()

        for python in self.python:
            if ( 
                termo_lower in python.especie.lower() or
                termo_lower in python.nome_popular.lower() or
                termo_lower in python.genero.lower() or
                termo_lower in python.descoberta.lower() or
                termo_lower in python.local.lower()):
                especies_encontradas.append(python)
        return especies_encontradas
    
    def listar_todas(self):
        if not self.python:
            print("Nenhuma espécie foi encontrada")
            return
        
        print('-' * 180)
        print("CATÁLOGO DE ESPÉCIES DO GÊNERO PYTHON")
        print('-' * 180)

        for i, python in enumerate(self.python, 1):
            print(f"{i}. {python}")

def exibir_resultados_pesquisa(especies_encontradas, termo_pesquisa):
    if especies_encontradas:
        print(f"\n ENCONTRADA(S) {len(especies_encontradas)} ESPÉCIE(S) PARA: '{termo_pesquisa}'")
        print('-' * 180)
        
        for i, python in enumerate(especies_encontradas, 1):
            print(f"{i}. {python}")
            print('-' * 180)
    else:
        print(f"\n ERRO: nenhuma espécie encontrada para o termo '{termo_pesquisa}'")
        print("Verifique se digitou o termo corretamente ou tente uma pesquisa diferente")

def menu_pesquisa(catalogo):
    while True:
        print("\n" +  "=" * 80)
        print("SISTEMA DE PESQUISA")
        print("=" * 80)
        print("")
        print("-" * 80)
        print("1. Pesquisa por espécie")
        print("-" * 80)
        print("2. Pesquisa por nome popular")
        print("-" * 80)
        print("3. Pesquisa por gênero")
        print("-" * 80)
        print("4. Pesquisa por Ano de Descoberta")
        print("-" * 80)
        print("5. Pesquisa por local de incidência")
        print("-" * 80)
        print("6. Pesquisa Geral")
        print("-" * 80)
        print("7. Listar todas as espécies")
        print("-" * 80)
        print("8. Sair")
        print("-" * 80)

        opcao = input("Escolha uma opção (1-8): ").strip()
        
        if opcao == '1':
            especie = input("Digite a espécie ou parte da espécie que você está procurando: ")
            resultados = catalogo.pesquisar_por_especie(especie)
            exibir_resultados_pesquisa(resultados, especie)

        elif opcao == '2':
            nome_popular = input("Digite o nome popular da espécie ou parte dele: ")
            resultados = catalogo.pesquisar_por_nome_popular(nome_popular)
            exibir_resultados_pesquisa(resultados, nome_popular)

        elif opcao == '3':
            genero = input("Digite o gênero da espécie a ser pesquisada: ")
            resultados = catalogo.pesquisar_por_genero(genero)  
            exibir_resultados_pesquisa(resultados, genero)
        
        elif opcao == '4':
            descoberta = input("Digite o ano de descoberta da espécie: ")
            resultados = catalogo.pesquisar_por_descoberta(descoberta)
            exibir_resultados_pesquisa(resultados, descoberta)

        elif opcao == '5':
            local = input("Digite o local em que a espécie possui maior incidência ou parte dele: ")
            resultados = catalogo.pesquisar_por_local(local)
            exibir_resultados_pesquisa(resultados, local)
        
        elif opcao == '6':
            termo = input("Digite o termo de pesquisa: ")
            resultados = catalogo.pesquisar_geral(termo)
            exibir_resultados_pesquisa(resultados, termo)
        
        elif opcao == '7':
            catalogo.listar_todas()
        elif opcao == '8':
            print("Obrigado por usar o sistema de catálogo!")
            break
        else: 
            print("Opção inválida! Escolha um número de 1 a 8 e tente novamente.")

if __name__ == "__main__":

    catalogo = Catalogo()

    especies_catalogo = [
        ("Píton Anchietae", "Píton-Angolana", "Python", "1887", "África"),
        ("Píton Curtus", "Píton-Sanguíneo", "Python", "1872", "Sudoeste da Ásia"),
        ("Píton Molurus", "Píton-Indiana", "Python", "1758", "Paquistão, Índia, Sri Lanka, sudeste da China..."),
        ("Píton Regius", "Píton-Real", "Python", "1802", "Senegal, Mali, Guiné, Serra Leoa..."),
        ("Píton Reticulatus", "Píton-Reticulada", "Python", "1801", "Sudeste da Ásia"),
        ("Píton Sebae", "Píton-Africana", "Python", "1788", "África"),
        ("Píton Timoriensis", "Píton-Timorense", "Python", "1876", "Indonésia")
    ]

    for especie_data in especies_catalogo:
        python_obj = Python(*especie_data) 
        catalogo.adicionar_python(python_obj)  
    
    print("SISTEMA INICIALIZANDO")
    print(f"Catálogo carregado com {len(catalogo.python)} espécies.")

    menu_pesquisa(catalogo)

              
               