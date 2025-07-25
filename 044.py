# Level 044

#  --------------
#  -- MULTADO? -- 
#  --------------
import random
print("-------------------------------------")
print("Você está dirigindo em uma rodovia...")
print("-------------------------------------")

velocidade = random.randint(5, 200)
if velocidade <= 20:
    print(f"Você foi multado por falta  de velocidade, sua velocidade era {velocidade}km/h")
elif velocidade >80 :
    print(f"Você foi multado por excesso de velocidade, sua falta de velocidade era {velocidade}km/h")
else:
    print(f"Você não foi multado, uau. Você estava dirigindo um total de {velocidade}km/h")