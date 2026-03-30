import numpy
from .sistema import criar_sistema, validar_sistema


def parse_numero(texto: str) -> float | None:
    """
    Converte uma string para float, substituindo vírgulas por pontos.
    Retorna None se a conversão falhar.

    Args:
        texto: string representando um número, podendo usar vírgula ou ponto como separador decimal

    Returns:
        float | None: valor numérico convertido, ou None se a conversão falhar
    """
    try:
        return float(texto.replace(",", "."))
    except ValueError:
        return None


def solicitar_tamanho_de_sistema() -> int:
    """
        Solicita ao usuário o tamanho do sistema (número de variáveis) e valida a entrada.

        Returns:
            int: O tamanho do sistema (número de variáveis).
    """
    while True:
        try:
            num = int(input("Digite o número de variáveis do sistema (máx. 10): "))
            if 1 <= num <= 10:
                return num
            print("Erro: O tamanho deve estar entre 1 e 10")
        except ValueError:
            print("Erro: Por favor, digite um número válido!")


def solicitar_sistema(tamanho: int) -> numpy.ndarray:
    """
        Solicita ao usuário os coeficientes e termos independentes de cada equação,
        preenchendo uma matriz aumentada (n x n+1).

        Utiliza criar_sistema() de sistema.py para alocar a matriz e
        validar_sistema() para garantir que a entrada é válida.

        Args:
            tamanho: número de equações do sistema.

        Returns:
            numpy.ndarray: matriz aumentada preenchida com os valores informados.
    """
    sistema = criar_sistema(tamanho)
    
    print(f"\n-- Preenchimento do sistema {tamanho}x{tamanho} --")
    for i in range(tamanho):
        print(f"Equação {i + 1}:")
        for j in range(tamanho):
            while True:
                entrada = input(f"  Coeficiente x{j + 1}: ")
                numero = parse_numero(entrada)
                if numero is not None:
                    sistema[i][j] = numero
                    break
                print("Por favor, digite somente números")

        while True:
            entrada = input(f"  Termo independente (b{i + 1}): ")
            numero = parse_numero(entrada)
            if numero is not None:
                sistema[i][tamanho] = numero
                break
            print("Por favor, digite somente números")
            
    return sistema


def imprimir_sistema(sistema: numpy.ndarray) -> None:
    """
       Imprime o sistema de equações de forma legível, mostrando os coeficientes e termos independentes.
       Será utilizada tanto para o sistema original quanto para o sistema escalonado.

       Args:
           sistema: matriz aumentada do sistema de equações.
    """
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
    """
        Exibe o resultado da resolução do sistema linear.
        - Se for um np.ndarray, imprime os valores de cada variável.
        - Se for uma string (SPI ou SI), imprime a mensagem correspondente.

        Args:
           resultado: vetor solução (np.ndarray) ou mensagem de classificação (str).
    """
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
