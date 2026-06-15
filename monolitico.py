import numpy as np

# input_output.py:
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


def solicitar_sistema(tamanho: int) -> np.ndarray:
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


def imprimir_sistema(sistema: np.ndarray) -> None:
    """
       Imprime o sistema de equações de forma legível, mostrando os coeficientes e termos independentes.
       Será utilizada tanto para o sistema original quanto para o sistema escalonado.

       Args:
           sistema: matriz aumentada do sistema de equações.
    """
    n = sistema.shape[0]
    m = sistema.shape[1]

    for i in range(n):
        linha = ""
        for j in range(m):
            valor = f"{sistema[i][j]:>8.2f}"
            if j == m - 1:
                linha += f" | {valor}"
            else:
                linha += valor
        print(linha)


def imprimir_resultado(resultado: np.ndarray | str) -> None:
    """
        Exibe o resultado da resolução do sistema linear.
        - Se for um np.ndarray, imprime os valores de cada variável.
        - Se for uma string (SPI ou SI), imprime a mensagem correspondente.

        Args:
           resultado: vetor solução (np.ndarray) ou mensagem de classificação (str).
    """
    print("\n" + "=" * 45)
    print(f"{'RESUMO DA SOLUÇÃO':^45}")
    print("=" * 45)

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

    print("=" * 45)


# sistema.py:


def criar_sistema(tamanho: int) -> np.ndarray:
    """
       Cria uma matriz de zeros com o tamanho especificado.

       Args:
           tamanho: número de equações (e variáveis) do sistema.

       Returns:
           np.ndarray: matriz aumentada (n x n+1) preenchida com zeros.

       Examples:
           >>> criar_sistema(3)
           array([[0., 0., 0., 0.],
                  [0., 0., 0., 0.],
                  [0., 0., 0., 0.]])
    """
    if tamanho <= 0 or tamanho > 10:
        raise ValueError("O tamanho deve estar entre 1 e 10.")

    return np.zeros((tamanho, tamanho + 1), dtype=float)


def copiar_sistema(sistema: np.ndarray) -> np.ndarray:
    """
    Cria uma cópia profunda da matriz aumentada para evitar
    modificações no sistema original.

    Args:
        sistema: matriz aumentada (n x n+1).

    Returns:
        np.ndarray: cópia independente da matriz recebida.
    """
    return np.copy(sistema)


def validar_sistema(sistema: np.ndarray) -> bool:
    """
        Verifica se a matriz possui o formato de sistema aumentado válido:
        - Deve ter forma (n x n+1), ou seja, uma coluna a mais que linhas.
        - Todos os elementos devem ser numéricos (int ou float).

        Args:
            sistema: matriz a ser validada.

        Returns:
            bool: True se o formato e os tipos forem válidos, False caso contrário.
    """
    # Verifica se é numpy array
    if not isinstance(sistema, np.ndarray):
        return False

    # Verifica se é 2D
    if sistema.ndim != 2:
        return False

    linhas, colunas = sistema.shape

    # Verifica formato n x (n+1)
    if colunas != linhas + 1:
        return False

    # Verifica se todos são números
    try:
        sistema.astype(float)
    except (ValueError, TypeError):
        return False

    return True


def obter_numero_de_variaveis(sistema: np.ndarray) -> int:
    """
    Retorna o número de variáveis do sistema linear, que corresponde
    ao número de linhas da matriz aumentada.

    Args:
        sistema: matriz aumentada (n x n+1).

    Returns:
        int: número de variáveis (n).
    """
    if not validar_sistema(sistema):
        raise ValueError("Sistema inválido.")

    return sistema.shape[0]


# escalonamento.py:


def escalonar_sistema(sistema: np.ndarray) -> np.ndarray:
    """
    Aplica a Eliminação de Gauss (escalonamento) na matriz aumentada,
    transformando-a em uma matriz triangular superior.

    Utiliza copiar_sistema() de sistema.py para não alterar a matriz original
    e obter_numero_de_variaveis() para determinar as dimensões do sistema.

    O processo deve ser implementado manualmente, sem usar numpy.linalg.

    Args:
        sistema: matriz aumentada (n x n+1) do sistema linear.

    Returns:
        np.ndarray: matriz aumentada escalonada (triangular superior).
    """
    mat = copiar_sistema(sistema).astype(float, copy=True)
    n = obter_numero_de_variaveis(mat)

    for i in range(n):
        linha_pivo = i
        for k in range(i + 1, n):
            if abs(mat[k, i]) > abs(mat[linha_pivo, i]):
                linha_pivo = k

        mat[[i, linha_pivo]] = mat[[linha_pivo, i]]

        if abs(mat[i, i]) < 1e-10:
            continue

        for k in range(i + 1, n):
            fator = mat[k, i] / mat[i, i]
            mat[k, i:] = mat[k, i:] - fator * mat[i, i:]

    return mat


# solver.py:


def classificar_sistema(sistema_escalonado: np.ndarray) -> str:
    """
    Analisa a matriz escalonada e classifica o sistema linear em:
    - "SPD" (Sistema Possível Determinado): solução única.
    - "SPI" (Sistema Possível Indeterminado): infinitas soluções.
    - "SI"  (Sistema Impossível): nenhuma solução.

    A classificação é feita verificando as linhas nulas da matriz
    escalonada e comparando com os termos independentes.

    Utiliza obter_numero_de_variaveis() de sistema.py para determinar
    as dimensões do sistema.

    Args:
        sistema_escalonado: matriz aumentada já escalonada (triangular superior).

    Returns:
        str: "SPD", "SPI" ou "SI".
    """
    n = obter_numero_de_variaveis(sistema_escalonado)

    linhas_nulas = 0
    for i in range(n):
        if np.allclose(sistema_escalonado[i, :n], 0):
            linhas_nulas += 1
            if not np.isclose(sistema_escalonado[i, n], 0):
                return "SI"

    if linhas_nulas > 0:
        return "SPI"

    return "SPD"


def substituicao_retroativa(sistema_escalonado: np.ndarray) -> np.ndarray:
    """
    Realiza a substituição retroativa na matriz escalonada para obter
    os valores de cada variável, partindo da última equação até a primeira.

    Pressupõe que o sistema já foi classificado como SPD.

    Utiliza obter_numero_de_variaveis() de sistema.py para determinar
    as dimensões do sistema.

    Args:
        sistema_escalonado: matriz aumentada escalonada (triangular superior).

    Returns:
        np.ndarray: vetor unidimensional com a solução de cada variável.
    """
    n = obter_numero_de_variaveis(sistema_escalonado)
    solucao = np.zeros(n)

    for i in range(n - 1, -1, -1):
        solucao[i] = sistema_escalonado[i, n]

        for j in range(i + 1, n):
            solucao[i] -= sistema_escalonado[i, j] * solucao[j]

        solucao[i] /= sistema_escalonado[i, i]

    return solucao


def resolver(sistema_escalonado: np.ndarray) -> np.ndarray | str:
    """
    Orquestra a resolução do sistema linear escalonado:
    1. Classifica o sistema usando classificar_sistema().
    2. Se SPD, resolve por substituição retroativa.
    3. Se SPI ou SI, retorna a mensagem correspondente.

    Args:
        sistema_escalonado: matriz aumentada já escalonada.

    Returns:
        np.ndarray: vetor solução se o sistema for SPD.
        str: mensagem descritiva se o sistema for SPI ou SI.
    """
    tipo = classificar_sistema(sistema_escalonado)

    if tipo == "SPD":
        return substituicao_retroativa(sistema_escalonado)
    elif tipo == "SPI":
        return "SPI"
    else:
        return "SI"


# main.py:


def main():
    tamanho_sistema = solicitar_tamanho_de_sistema()
    sistema = solicitar_sistema(tamanho_sistema)
    print("\nMatriz Aumentada [A|b]:")
    imprimir_sistema(sistema)

    sistema_escalonado = escalonar_sistema(sistema)
    print("\nMatriz Escalonada [A|b]:")
    imprimir_sistema(sistema_escalonado)

    resultado = resolver(sistema_escalonado)
    imprimir_resultado(resultado)


if __name__ == "__main__":
    main()
main()
