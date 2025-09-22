# Level 078
# -------------------------
# -- CATÁLOGO BIBLIOTECA --
# -------------------------

class Livro: 
    def __init__(self, titulo, autor, genero, ano, ISBN):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.ano = ano
        self.ISBN = ISBN 

    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Gênero: {self.genero}, Ano: {self.ano}, ISBN: {self.ISBN}"

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)
    
    def pesquisar_por_titulo(self, titulo_pesquisa):
        livros_encontrados = []
        for livro in self.livros:
            if titulo_pesquisa.lower() in livro.titulo.lower():
                livros_encontrados.append(livro)
        return livros_encontrados
    
    def pesquisar_por_autor(self, autor_pesquisa):
        livros_encontrados = []
        for livro in self.livros:
            if autor_pesquisa.lower() in livro.autor.lower():
                livros_encontrados.append(livro)
        return livros_encontrados
    
    def pesquisar_por_ano(self, ano_pesquisa):
        livros_encontrados = []
        for livro in self.livros:
            if ano_pesquisa.strip() == livro.ano.strip():
                livros_encontrados.append(livro)
        return livros_encontrados
            
    def pesquisar_por_genero(self, genero_pesquisa):
        livros_encontrados = []
        for livro in self.livros:
            if genero_pesquisa.lower() in livro.genero.lower():
                livros_encontrados.append(livro)
        return livros_encontrados

    def pesquisar_por_ISBN(self, isbn_pesquisa):
        livros_encontrados = []
        for livro in self.livros:
            if isbn_pesquisa.strip() == livro.ISBN.strip():
                livros_encontrados.append(livro)
        return livros_encontrados 

    def pesquisar_geral(self, termo_pesquisa):
        livros_encontrados = []
        termo_lower = termo_pesquisa.lower()

        for livro in self.livros:
            if (termo_lower in livro.titulo.lower() or
                termo_lower in livro.autor.lower() or
                termo_lower in livro.genero.lower() or
                termo_lower in livro.ISBN.lower() or
                termo_lower in livro.ano.lower()):
                livros_encontrados.append(livro)
        return livros_encontrados
    
    def listar_todos_livros(self):
        if not self.livros:
            print("Nenhum livro foi encontrado.")
            return
    
        print('-' * 180)
        print("CATÁLOGO COMPLETO DA BIBLIOTECA")
        print('-' * 180)

        for i, livro in enumerate(self.livros, 1):
            print(f"{i}. {livro}")
            print('-' * 180)
    
def exibir_resultados_pesquisa(livros_encontrados, termo_pesquisa):
        if livros_encontrados:
            print(f"\n ENCONTRADO(S) {len(livros_encontrados)} LIVRO(S) PARA: '{termo_pesquisa}'")
            print('-' * 180)
    
            for i, livro in enumerate(livros_encontrados, 1):
                print(f"{i}. {livro}")
                print('-' * 180)
        else:
            print(f"\n ERRO: Nenhum livro encontrado para '{termo_pesquisa}'")
            print("Verifique se digitou corretamente ou tente uma pesquisa diferente.")
    
def menu_pesquisa(biblioteca):
        while True:
            print("\n" +  "=" * 80)
            print("SISTEMA DE PESQUISA DA BIBLIOTECA")
            print("=" * 80)
            print("")
            print("-" * 80)
            print("1. Pesquisar por título")
            print("-" * 80)
            print("2. Pesquisar por autor")
            print("-" * 80)
            print("3. Pesquisar por gênero")
            print("-" * 80)
            print("4. Pesquisar por ano")
            print("-" * 80)
            print("5. Pesquisar por ISBN")
            print("-" * 80)
            print("6. Pesquisa geral (título, autor, gênero, ano, ISBN)")
            print("-" * 80)
            print("7. Listar todos os livros")
            print("-" * 80)
            print("8. Sair")
            print("-" * 80)

            opcao = input("Escolha uma opção (1-8): ").strip()

            if opcao == "1":
                titulo = input("Digite o título ou parte do título: ")
                resultados = biblioteca.pesquisar_por_titulo(titulo)
                exibir_resultados_pesquisa(resultados, titulo)
            
            elif opcao == "2":
                autor = input("Digite o nome do autor ou parte do nome do autor: ")
                resultados = biblioteca.pesquisar_por_autor(autor)
                exibir_resultados_pesquisa(resultados, autor)       
            elif opcao == "3":
                genero = input("Digite o gênero do livro: ")
                resultados = biblioteca.pesquisar_por_genero(genero)
                exibir_resultados_pesquisa(resultados, genero)
            elif opcao == "4":
                ano = input("Digite o ano do livro: ")
                resultados = biblioteca.pesquisar_por_ano(ano)
                exibir_resultados_pesquisa(resultados, ano)
            elif opcao == "5":
                ISBN = input("Digite o ISBN do livro ou parte do ISBN: ")
                resultados = biblioteca.pesquisar_por_ISBN(ISBN)
                exibir_resultados_pesquisa(resultados, ISBN)
            elif opcao == "6":
                termo = input("Digite o termo de pesquisa: ")
                resultados = biblioteca.pesquisar_geral(termo)
                exibir_resultados_pesquisa(resultados, termo)
            elif opcao == "7":
                 biblioteca.listar_todos_livros()
            elif opcao == "8":
                print("Obrigado por usar o sistema da biblioteca!")
                break
            else:
                print("Opção inválida! Escolha um número de 1 a 8.")

if __name__ == "__main__":
    
    biblioteca = Biblioteca()
    
    livros_catalogo = [
        ("Pensamento Crítico - o poder da lógica e da argumentação", "Walter A. Carnielli, Richard L. Epstein", "Educativo", "2019", "978-8533954403"),
        ("Como não Perder a Cabeça - auto-educação clássica contra a doutrinação cultural", "Deal W. Hudson", "Continuação da educação", "2021", "978-6587404257"),
        ("Os Elementos da Filosofia Moral", "James Rachels, Stuart Rachels", "Filosofia Política", "2013", "978-8580552331"),
        ("Um Convite a Filosofia", "Marilena Chauí", "Filosofia infanto juvenil", "2019", "978-8508134694"),
        ("O Mito de Sísifo", "Albert Camus", "Lógica e Linguagem Política e Ciências Sociais", "2018", "978-8501111647"),
        ("Livre para Escolher", "Milton Friedman, Rose Friedman", "Economia", "2015", "978-8501103666"),
        ("Manual de Debate Político", "Kim Kataguri", "Política", "2021", "978-6586618679"),
        ("O Príncipe", "Maquiavel", "Política", "1513", "978-6584956193"),
        ("Estatística - o que é, para que serve e como funciona", "Charles Wheelan", "Estatística", "2016", "978-8537815120"),
        ("Viver com Risco - como enfrentar as situações incertas da vida cotidiana", "Allison Schrager", "Tomar decisões", "2021", "978-8582851364") ]

    for catalogo in livros_catalogo:
        livro = Livro(*catalogo)
        biblioteca.adicionar_livro(livro)

    print("SISTEMA DE BIBLIOTECA INICIALIZANDO")
    print(f"Catálogo carregado com {len(biblioteca.livros)} livros.")

    menu_pesquisa(biblioteca)