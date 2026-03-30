import numpy
from src.sistema import criar_sistema, validar_sistema


def solicitar_tamanho_de_sistema() -> int:
    while True:
        try:
            num = int(input("Digite o número de variáveis do sistema (máx. 10): "))
            if 1 <= num <= 10:
                return num
            print("Erro: O tamanho deve estar entre 1 e 10")
        except ValueError:
            print("Erro: Por favor, digite um número válido!")

def solicitar_sistema(tamanho: int) -> numpy.ndarray:
    sistema = criar_sistema(tamanho)
    
    print(f"\n-- Preenchimento do sistema {tamanho}x{tamanho} --")
    for i in range(tamanho):
        print(f"Equação {i + 1}:")
        for j in range(tamanho):
            while True:
                val = input(f"  Coeficiente x{j + 1}: ")
                if validar_sistema(val):
                    sistema[i][j] = float(val)
                    break
                print("Por favor, digite somente números")
        
        while True:
            termo_ind = input(f"  Termo independente (b{i + 1}): ")
            if validar_sistema(termo_ind):
                sistema[i][tamanho] = float(termo_ind)
                break
            print("Por favor, digite somente números")
            
    return sistema

def imprimir_sistema(sistema: numpy.ndarray) -> None:
    n = sistema.shape[0]
    m = sistema.shape[1]
    
    print("\nMatriz Aumentada [A|b]:")
    for i in range(n):
        linha = ""
        for j in range(m):
            valor = f"{sistema[i][j]:>8.2f}"
            if j == m - 1:
                linha += f" | {valor}"
            else:
                linha += valor
        print(linha)

def imprimir_resultado(resultado: numpy.ndarray | str) -> None:
    print("\n" + "="*45)
    print(f"{'RESUMO DA SOLUÇÃO':^45}")
    print("="*45)

    # se for string (classificação de SI ou SPI):
    if type(resultado) == str:
        if resultado == "SI":
            print("Status: [SI] Sistema Impossível")
            print("Motivo: O sistema não possui nenhuma solução real")
        elif resultado == "SPI":
            print("Status: [SPI] Sistema Possível e Indeterminado")
            print("Motivo: O sistema possui infinitas soluções")
        else:
            print(f"Status: {resultado}")
    
    # se for array (vetor gerado no caso de SPD):
    else:
        print("Status: [SPD] Sistema Possível e Determinado")
        print("-" * 45)
        print("Valores das variáveis:")
        for i, valor in enumerate(resultado):
            # formatação com 4 casas decimais
            print(f"  x{i + 1} = {valor:>10.4f}")
            
    print("="*45)