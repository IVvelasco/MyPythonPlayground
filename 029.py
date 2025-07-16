# Level 018

#  -------------------------------
#  -- SIMULADOR DE FICHA MÉDICA --
#  -------------------------------

print("Aqui vamos simular algumas perguntas básicas que as enfermeiras fazem quando estão fazendo a triagem dos pacientes.")

nome_completo = input("O nome completo do paciente é: ")
tipo_doc = input("Esse é o CPF do paciente ou o Cartão do SUS?")
documento = int(input("Documento do paciente, por favor responda apenas com números: "))
idade = int(input("Idade do paciente: "))
cidade = input("Cidade em que o paciente reside: ")
sexo = input("Responda F para feminino e M para masculino: ")
rua = input("A residência do paciente fica na rua: ")
num_casa = int(input("Número da residência: "))
bairro = input("Bairro onde o paciente mora: ")
cep = int(input("CEP da residência, por favor responda apenas com números: "))
telefone = int(input("Qual é o número de telefone do paciente? Por favor, apenas números: "))
entrada = float(input("Horário de entrada: "))
data_de_entrada = input("Insira a data de entrada do paciente, respeitando o seguinte formato: 00/00/0000: ")
queixas = input("Quais são as queixas do paciente? Insira aqui: ")
print("-------------------------------------------------------------------------------------------------------------------------------------------------------")
print("----------------------------------------------------------FICHA MÉDICA---------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------------------------------------------------------------------------------")
print(f"NOME COMPLETO DO PACIENTE: {nome_completo}") 
print("-------------------------------------------------------------------------------------------------------------------------------------------------------")
print(f"DOCUMENTO (CPF OU CARTÃO DO SUS): {tipo_doc}, número: {documento}")
print("-------------------------------------------------------------------------------------------------------------------------------------------------------")
print(f"IDADE DO PACIENTE: {idade} ----------------------------------------------------------------------------------------------------SEXO: {sexo} ---------------------") 
print("-------------------------------------------------------------------------------------------------------------------------------------------------------")
print(f"Cidade onde Reside: {cidade} --- Rua: {rua}, de número {num_casa}, no Bairro {bairro} e CEP: {cep}")
print(f"-------------------------------------------------------------------------------------------------------------------------------------------------------")
print(f"Número de telefone para contato: {telefone}")
print("-------------------------------------------------------------------------------------------------------------------------------------------------------")
print(f"Horário de entrada: {entrada}")
print("-------------------------------------------------------------------------------------------------------------------------------------------------------")
print(f"Data de entrada: {data_de_entrada}")
print("-------------------------------------------------------------------------------------------------------------------------------------------------------")
print(f"Queixas do paciente: {queixas}")
print("-------------------------------------------------------------------------------------------------------------------------------------------------------")


""" ABSTRAÇÕES FEITAS APÓS CONVERSAR COM UMA ENFERMEIRA 
-->  Nome completodo paciente OK 
-->  Documento (tipo cartão do SUS ou CPF ) OK 
-->  Número de telefone OK
-->  Data de nascimento OK
-->  Masculino ou feminino OK 
-->  Idade OK 
-->  Onde reside (rua, bairro e cidade) OK 
-->  Horário que chegou OK
-->  Data OK 
-->  Verficação dos sinais vitais
-->  Quais são as queixas do paciente
-->  Se ele é alérgico a alguma medicação

----------------------------------------------------------------------------------------------
FEITO ISSO O PACIENTE É ENCAMINHADO DIRETAMENTE PARA A SALA DE ESPERA OU DIRETAMENTE AO MÉDICO
----------------------------------------------------------------------------------------------
"""