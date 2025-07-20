# Level 014
# ----------------------------
# -- MÉDIA E DESVIO PADRÃO --
# ----------------------------
import numpy as np
"""
DADOS CLIMÁTICOS RETIRADOS DIRETAMENTE DO MINISTÉRIO DA AGRICULTURA, PECUÁRIA E ABASTECIMENTO - MAPA
Instituto Nacional de Meteorologia – INMET
Coordenação-Geral de Meteorologia Aplicada, Desenvolvimento e Pesquisa - CGMADP
Centro de Análise e Previsão do Tempo - CAPRE
Porto Alegre, 25 de fevereiro de 2025
BOLETIM CLIMATOLÓGICO
BALANÇO DO MÊS DE JANEIRO DE 2025 PARA PORTO ALEGRE.
"""

# DADOS
temp_max = np.array([31, 32, 30, 29, 30, 31, 32, 30, 29, 30, 31, 33, 35, 35, 34, 33, 35, 34, 35, 34, 33, 34, 34, 33, 32, 30, 31, 32, 33, 32, 31])
temp_min = np.array([23, 22, 21, 20, 19, 18, 17, 19, 20, 19, 20, 21, 22, 23, 22, 21, 22, 21, 20, 21, 22, 21, 20, 19, 20, 21, 22, 21, 22, 21, 21])

# CÁLCULO DA MÉDIA
media0 = np.mean(temp_max)
media1 = np.mean(temp_min)

# CÁLCULO DO DESVIO PADRÃO
desvio_padrao0 = np.std(temp_max)
desvio_padrao1 = np.std(temp_min)

# OUTPUT

print("----------------------------------------------------------------------------------------------------------------------------------------")
print(f"DADOS TRABALHADOS SOBRE A TEMPERATURA MÁXIMA: {temp_max}")
print("----------------------------------------------------------------------------------------------------------------------------------------")
print(f"MÉDIA: {media0:.2f}")
print("----------------------------------------------------------------------------------------------------------------------------------------")
print(f"DESVIO PADRÃO: {desvio_padrao0:.2f}")
print("----------------------------------------------------------------------------------------------------------------------------------------")
print("")

print("")
print("----------------------------------------------------------------------------------------------------------------------------------------")
print(f"DADOS TRABALHADOS SOBRE A TEMPERATURA MÍNIMA: {temp_min}")  
print("----------------------------------------------------------------------------------------------------------------------------------------")
print(f"MÉDIA: {media1:.2f}")
print("----------------------------------------------------------------------------------------------------------------------------------------")
print(f"DESVIO PADRÃO: {desvio_padrao1:.2f}")
print("----------------------------------------------------------------------------------------------------------------------------------------")
