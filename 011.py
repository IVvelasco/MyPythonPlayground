# Level 011

# ---------------------------
# -- BRINCADEIRA DE ESCOLA --
# ---------------------------

import random 
"""
Mini Game baseado naquelas brincadeiras de escola tipo quantos filhos você terá, com quem vai casar e etc etc.
"""

idade = random.randint(18,100)
print(f"Idade que você se casou: {idade}")

numero = random.randint(1, 1000)
print(f"Número de encontros que você teve antes de encontrar a pessoa certa: {numero}")

local = ["Parque", "Restaurante Japonês", "Cinema", "Apartamento", "Restaurante Italiano", "Dogão da Esquina", "Estádio de Futebol", "Shopping"]
print(f"No dia do encontro vocês foram para um: {random.choice(local)}")

inicial = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
print(f"O nome da sua alma gêmea começa com a letra: {random.choice(inicial)}")

cantada = ["Se beleza fosse merda você tava toda cagada", "Ó Lua, quero amar-te", "Numa chuva de beijos eu saio sem guarda-chuva", "Você é a minha música da Sabrina Carpender", "Are you gringo?", "Quero que eu próximo CEP seja o da sua casa", "Não sou pirata mas se quiser pode andar na prancha", "Bora ver Netflix lá em casa?", "Pesquisei por perfeição no dicionário e nos exemplos vi uma foto sua", "E se a gente fugisse juntos?", "Pspspspspspspspspssp", "Fiu fiuuuu"]
print(f"Ele te conquistou quando sussurrou no seu ouvido: {random.choice(cantada)}")

desculpa = ["Meu peixe está se afogando", "Esqueci o ferro ligado", "Esqueci que não posso tirar a tornozeleira eletrônica", "Esqueci de passar aspirador no carpete" ,"Hoje é aniversário do meu Hamster", "Minha Vó tá no bingo e eu fiquei de buscar", "Minha esposa tá me ligando", "Preciso ir jogar no bicho antes que a banca feche", "As vozes me disseram que você é batatinha", "Eu tenho uma reunião mais tarde", "Parece que estou sonhando então vou tentar voar", "Alguém precisa ensinar palavrão pro meu papagaio", "Esqueci que sou padre e hoje tenho batizado", "Esqueci onde estacionei o carro, já volto", "Tenho que ver replay do Botafogo ganhando do PSG", "Acabou a seda"]
print(f"A desculpa que a sua alma gêmea deu para ir embora do primeiro encontro foi: {random.choice(desculpa)}")

hora = random.randint(1, 24)
minutos = random.randint(1, 60)
print(f"O encontro iniciou lá pelas {hora} e {minutos}")

Hora = random.randint(1, 24)
Minutos = random.randint(1, 60)
print(f"E terminou lá pelas {Hora} e {Minutos} ")

religiao = ["Cristianismo", "Islamismo", "Macumbeiro", "Umbandista", "Espírita", "Budista", "Hindu", "Xintoísmo", "Evangélico", "Judaísmo", "Confucionismo", "Wicca", "Satanismo", "Jovem Místico", "Astrólogo", "Tarólogo"]
print(f"Para casarem você se converteu ao: {random.choice(religiao)}")

desapontamento = ["Vó", "Manuel da Padaria","Computador", "Hacker Russo", "Mãe", "Pai", "Ex", "Amigos", "Parentes distantes", "Primo", "Melhor amiga", "Vizinho", "Veia rádio patrulha", "Cara da Padaria", "Gato", "Cachorro da vizinha", "Melhor Amigo", "Assaltante", "Padre da Quermesse", "Vendedor de Amendoim", "Ex-Chefe", "Gerente do Hotel", "Amigo pra quem vocês devem dinheiro", "Manicure", "Véio da Havan"]
print(f"Quem ficou mais desapontado com o casamento: {random.choice(desapontamento)}")

testemunha = ["Vó", "Manuel da Padaria","Computador", "Hacker Russo", "Mãe", "Pai", "Ex", "Amigos", "Parentes distantes", "Primo", "Melhor amiga", "Vizinho", "Veia rádio patrulha", "Cara da Padaria", "Gato", "Cachorro da vizinha", "Melhor Amigo", "Assaltante", "Padre da Quermesse", "Vendedor de Amendoim", "Ex-Chefe", "Gerente do Hotel", "Amigo pra quem vocês devem dinheiro", "Manicure", "Véio da Havan"]
print(f"Quem serviu de testemunha na hora de assinar: {random.choice(testemunha)}")

mes = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
print(f"O casamento ocorreu no mês de: {random.choice(mes)}")

jogo = ["Roleta Russa", "UNO", "Truco", "Strip Poker", "Futebol", "Xadrez", "Kama Sutra", "Frescobol", "Cabra cega", "Pega-Pega", "Esconde-Esconde", "Damas", "RPG", "Video Game", "Qualquer jogo da Steam", "BlackJack", "Poker", "Uno", "Truco", "Jogos de Tabuleiro", "Verdade ou Consequência"]
print(f"Até hoje vocês adoram jogar {random.choice(jogo)} juntos")






