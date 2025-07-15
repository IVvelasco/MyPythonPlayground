# Level 020

#  ---------------
#  -- SHOPPING  --
#  ---------------

import random

print("=============================================")
print("= Vamos simular uma voltinha pelo shopping! =")
print("=============================================")
print("")

chegada = ["o uber te trouxe", "foi de ônibus", "recebeu carona", "foi andando", "deu spawn", "seguiu de moto"]
task0 = print(f"Você chegou ao shopping pois {random.choice(chegada)} ")
if random.choice(task0) == "o uber te trouxe":
    print("A corrida foi cara mas o motorista era gente boa")
elif random.choice(task0) == "foi de ônibus":
    print("Parecia uma lata de sardinha e você chegou suado e exausto")
elif random.choice(task0) == "recebeu carona":
    print("E o mais engraçado disso tudo é que você nem conhecia o cara")
elif random.choice(task0) == "foi andando":
    print("E agora seus pés  estão doendo. Que ideia foi essa de ir andando 10 km de salto alto?")
elif random.choice(task0) == "deu spawn":
    print("Você espirrou e deu spawn no shopping")
elif random.choice(task0) == "seguiu de moto":
    print("E ainda recebeu multa por excesso de velocidade")


piso0 = ["ir pelas escadas", "esperar pelo elevador", "fazer parkour", "permitir que um estranho te levasse nas costas", "se esconder em um carrinho de bebê", "subir uma rampa"]
print(f"Você foi até o térreo e para isso decidiu {random.choice(piso0)}")
if random.choice(piso0) == "ir pelas escadas":
    print("Essa foi a cardio do dia")
elif random.choice == "esperar pelo elevador":
    print("Você ficou preso no elevador por 30 minutos")
elif random.choice(piso0) == "fazer parkour":
    print("Você caiu feio e por sorte não quebrou nada")
elif random.choice(piso0) == "permitir que um estranho te levasse nas costas":
    print("Você deveria repensar suas escolhas, jovem")
elif random.choice(piso0) == "se esconder em um carrinho de bebê":
    print("Só deu certo porque era um bebê reborn")
elif random.choice(piso0) == "subir uma rampa":
    print(" Você acabou parando no lugar errado e precisou refazer todo o caminho")
print("")

piso1 = ["a loja de roupas femininas", "a loja de roupas masculina", "a loja de calçados", "a loja de produtos eletrônicos", "a loja de acessórios e bolsas", "uma livraria"]
print(f"Dentro do shopping você optou por ir direto até {random.choice(piso1)}")
if random.choice(piso1) == "a loja de roupas femininas":
    print("Você aproveitou para comprar umas calcinhas")
elif random.choice(piso1) == "a loja de roupas masculinas":
    print("Você comprou um belo cinto")
elif random.choice(piso1) == "a loja de calçados":
    print("Você disse ao vendedor que só estava dando uma olhadinha")
elif random.choice(piso1) == "a loja de produtos eletrônicos":
    print("Você estourou o limite do cartão e valeu cada centavo")
elif random.choice(piso1) == "a loja de acessórios e bolsas":
    print("Você achou tudo muito caro e de péssima qualidade mas mesmo assim comprou uma carteira")
elif random.choice(piso1) == "uma livraria":
    print("Você cheirou todos os livros e o vendedor te pediu para ir sair")
print("")

piso2 = ["visitou a loja de roupas infantis", "encontrou um cachorro perdido", "encontrou um gato perdido", "parou numa das cadeiras de massagem", "viu o namorado da sua amiga com outra", "teve dificuldade de usar a escada rolante"]
print(f"Chegando ao outro piso você {random.choice(piso2)}")
if random.choice(piso2) == "Visitou a loja de roupas infantis":
    print("Agora seu bebê reborn tem novas roupas!")
elif random.choice(piso2) == "encontrou um cachorro perdido":
    print("O cachorro te mordeu, foi a maior confusão para encontrar o dono mas pelo menos você não precisou tomar nenhuma vacina")
elif random.choice(piso2) == "encontrou um gato perdido":
    print("Você e seu novo gato foram ao petshop para um tratamento completo!")
elif random.choice(piso2) == "parou numa das cadeiras de massagem":
    print("O massagista pediu o número do seu telefone e você saiu correndo")
elif random.choice == "viu o namorado da sua amiga com outra":
    print("Você tirou muitas fotos e sua amiga entrou num uber para pegar ele no flagra")
elif random.choice(piso2) == "teve dificuldade de usar a escada rolante":
    print("Você precisou usar as escadas normais e chegou quase sem fôlego na praça de alimentação")
print("")

piso3 = ["comer um hambúrguer", "comer comida caseira", "beber um milkshake", "não comer nada", "ir direto para a sobremesa", "pedir 10 esfirras", "comer uma pizza inteira"]
print(f"Finalmente você está na tão querida praça de alimentação, você decide {random.choice(piso3)}")
if random.choice(piso3) == "comer um hambúrguer":
    print("O preço estava salgado mas foi delicioso")
elif random.choice(piso3) == "comer comida caseira":
    print("Vocẽ percebeu que era só comida congelada super-faturada ")
elif random.choice(piso3) == "beber um milkshake":
    print("Você é intolerante a lactose e precisou ir correndo no banheiro")
elif random.choice(piso3) == "não comer nada":
    print("Economizar é bom mas seu nível de açúcar está muito baixo")
elif random.choice(piso3) == "ir direto para a sobremesa":
    print("Quem nunca? A sobremesa estava uma delícia")
elif random.choice(piso3) == "pedir 10 esfirras":
    print("Você acabou pedindo mais 10 para levar pra casa")
elif random.choice(piso3) == "comer uma pizza inteira":
    print("Pena que a pizzaria estava fechada")
