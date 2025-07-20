# Level 015
# ------------------------------------------------
# -- MODA, MÉDIA E MEDIANA USANDO NUMPY e SCIPY --
# ------------------------------------------------

# E de bônus ainda vamos calcular o DESVIO PADRÃO

import numpy as np
from scipy import stats

def main():
    # Coletar múltiplos valores do usuário
    print("Digite os dados separados por vírgula (ex: 31,32,30,29):")
    entrada = input("Declare aqui os dados que você quer analisar: ")
    
    # Converter a string em lista de números
    try:
        # Divide por vírgula, remove espaços e converte para float
        dados_lista = [float(i.strip()) for i in entrada.split(',')]
        dados = np.array(dados_lista)
    except Exception:
        print("Erro: Verifique se os dados foram inseridos corretamente.")
        return
    
    # CÁLCULO DA MÉDIA
    media = np.mean(dados)
    
    # CÁLCULO DO DESVIO PADRÃO
    desvio_padrao = np.std(dados)
    
    # CÁLCULO DA MEDIANA
    mediana = np.median(dados)
    
    # CÁLCULO DA MODA
    moda_resultado = stats.mode(dados, keepdims=True)
    moda = moda_resultado.mode[0]
    
    # OUTPUT
    print("----------------------------------------------------------------------------------------------------------------------------------------")
    print(f"DADOS TRABALHADOS: {dados_lista}")
    print("----------------------------------------------------------------------------------------------------------------------------------------")
    print("")
    print("----------------------------------------------------------------------------------------------------------------------------------------")
    print(f"MÉDIA: {media:.2f}")
    print("----------------------------------------------------------------------------------------------------------------------------------------")
    print("")
    print("----------------------------------------------------------------------------------------------------------------------------------------")
    print(f"MEDIANA: {mediana:.2f}")
    print("----------------------------------------------------------------------------------------------------------------------------------------")
    print("")
    print("----------------------------------------------------------------------------------------------------------------------------------------")
    print(f"MODA: {moda:.2f}")
    print("----------------------------------------------------------------------------------------------------------------------------------------")
    print("")
    print("----------------------------------------------------------------------------------------------------------------------------------------")
    print(f"DESVIO PADRÃO: {desvio_padrao:.2f}")
    print("----------------------------------------------------------------------------------------------------------------------------------------")

# Chamar a função principal
if __name__ == "__main__":
    main()
