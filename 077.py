# Level 077

# -------------------------
# -- CATÁLOGO BIBLIOTECA --
# -------------------------


class livrodef:
    def __init__(self, titulo, autor, genero, ano, ISBN):
        self.nome = titulo
        self.autor = autor
        self.genero = genero
        self.ano = ano
        self.ISBN = ISBN   
if __name__ == "__main__":
    livro0 = livrodef("Pensamento Crítico - o poder da lógica e da argumentação", " Walter A. Carnielli, Richard L. Epstein","Educativo", "2019" ,"978-8533954403 ")
    print('-' * 178)
    print(f"Nome:{livro0.nome}, autor: {livro0.autor}, gênero: {livro0.genero}, ano: {livro0.ano} e ISBN: {livro0.ISBN} ")
    print('-' * 178)
    livro1 = livrodef("Como não Perder a Cabeça - auto-educação clássica contra a doutrinação cultural ", "Deal W. Hudson","Continuação da educação","2021" ,"978-6587404257")
    print(f"Nome:{livro1.nome}, autor: {livro1.autor}, gênero: {livro1.genero}, ano: {livro1.ano} e ISBN: {livro1.ISBN} ")
    print('-' * 178)
    livro2 = livrodef("Os Elementos da Filosofia Moral", "James Rachels, Stuart Rachels","Filosofia Política","2013" ,"978-8580552331")
    print(f"Nome:{livro2.nome}, autor: {livro2.autor}, gênero: {livro2.genero}, ano: {livro2.ano} e ISBN: {livro2.ISBN} ")
    print('-' * 178)
    livro3 = livrodef("Um Convite a Filosofia", "Marilena Chauí","Filosofia infanto juvenil","2019" ,"978-8508134694")
    print(f"Nome:{livro3.nome}, autor: {livro3.autor}, gênero: {livro3.genero}, ano: {livro3.ano} e ISBN: {livro3.ISBN} ")
    print('-' * 178)
    livro4 = livrodef("O Mito de Sísifo", "Albert Camus"," Lógica e Linguagem Política e Ciências Sociais","2018" ,"978-8501111647")
    print(f"Nome:{livro4.nome}, autor: {livro4.autor}, gênero: {livro4.genero}, ano: {livro4.ano} e ISBN: {livro4.ISBN} ")
    print('-' * 178)
    livro5 = livrodef("Livre para Escolher", "Milton Friedman, Rose Friedman","Economia","2015" ,"978-8501103666")
    print(f"Nome:{livro5.nome}, autor: {livro5.autor}, gênero: {livro5.genero}, ano: {livro5.ano} e ISBN: {livro5.ISBN} ")
    print('-' * 178)
    livro6 = livrodef(" Manual de Debate Político", "Kim Kataguri","Política","2021" ,"978-6586618679")
    print(f"Nome:{livro6.nome}, autor: {livro6.autor}, gênero: {livro6.genero}, ano: {livro6.ano} e ISBN: {livro6.ISBN} ")
    print('-' * 178)
    livro7 = livrodef("O Príncipe", "Maquiavel","Política","1513" ,"978-6584956193")
    print(f"Nome:{livro7.nome}, autor: {livro7.autor}, gênero: {livro7.genero}, ano: {livro7.ano} e ISBN: {livro7.ISBN} ")
    print('-' * 178)
    livro8 = livrodef("Estatística - o que é, para que serve e como funciona", "Charles Wheelan","Estatística","2016" ,"978-8537815120")
    print(f"Nome:{livro8.nome}, autor: {livro8.autor}, gênero: {livro8.genero}, ano: {livro8.ano} e ISBN: {livro8.ISBN} ")
    print('-' * 178)
    livro9 = livrodef("Viver com Risco - como enfrentar as situações incertas da vida cotidiana ", "Allison Schrager","Tomar decisões","2021" ,"978-8582851364")
    print(f"Nome:{livro9.nome}, autor: {livro9.autor}, gênero: {livro9.genero}, ano: {livro9.ano} e ISBN: {livro9.ISBN} ")
    print('-' * 178)
