# Level 006

# ---------------
# -- IF - ELSE --
# ---------------

# Level 006

print("Bem-vindo ao menu que faz a média das suas notas!")

matematica = float(input("Sua nota de Matemática: "))
geografia = float(input("Sua nota de Geográfia: "))
fisica = float(input("Sua nota de Física: "))
portugues = float(input("Sua nota de Português: "))
quimica = float(input("Sua nota de Química : "))
historia = float(input("Sua nota de História: "))
literatura = float(input("Sua nota de Literatura: "))
artes = float(input("Sua nota de Artes: "))

nota_total = matematica + geografia + fisica + portugues + quimica + historia + literatura + artes
media = nota_total / 8 

if media  >= 70:
    print("Parabéns, você passou!Sua média é ", media)
else: 
    print("Que triste! Sua média é: ", media)
