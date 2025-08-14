# Level 037

#  -----------------------------------------
#  -- TEMPERATURA EM CELSIUS E FAHRENHEIT --
#  -----------------------------------------

unidade = input("Essa teperatura será em Celsius ou Fahrnheit? (F/C): ")
temperatura = float(input("Insira a temperatura: "))

if unidade == "C":
    conversor = round((9 * temperatura) / 5 + 32)
    print(f"A temperatura de {temperatura} graus Celsius corresponde a {conversor:.2f} graus Fahrnheit")
elif unidade == "c":
    conversor = round((9 * temperatura) / 5 + 32)
    print(f"A temperatura de {temperatura} graus Celsius corresponde a {conversor:.2f} graus Fahrnheit")
elif unidade == "F":
    conversor_c = ((temperatura - 32) * 5 / 9)
    print(f"A temperatura de {temperatura} graus Fahrnheit corresponde a {conversor_c.:2f} graus Celsius")
elif unidade == "f":
    conversor_c = ((temperatura - 32) * 5 / 9)
    print(f"A temperatura de {temperatura} graus Fahrnheit corresponde a {conversor_c:.2f} graus Celsius")
else:
    print("Esse não é um valor válido, por favor escolha entre F ou C ")
