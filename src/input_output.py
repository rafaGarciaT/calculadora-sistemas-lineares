import numpy
from src.sistema import criar_sistema, validar_sistema


def solicitar_tamanho_de_sistema() -> int:
    """
    Solicita ao usuário o tamanho do sistema (número de variáveis) e valida a entrada.

    Returns:
        int: O tamanho do sistema (número de variáveis).
    """
    pass

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
    pass

def imprimir_sistema(sistema: numpy.ndarray) -> None:
    """
    Imprime o sistema de equações de forma legível, mostrando os coeficientes e termos independentes.
    Será utilizada tanto para o sistema original quanto para o sistema escalonado.

    Args:
        sistema: matriz aumentada do sistema de equações.
    """
    pass

def imprimir_resultado(resultado: numpy.ndarray | str) -> None:
    """
    Exibe o resultado da resolução do sistema linear.
    - Se for um np.ndarray, imprime os valores de cada variável.
    - Se for uma string (SPI ou SI), imprime a mensagem correspondente.

    Args:
       resultado: vetor solução (np.ndarray) ou mensagem de classificação (str).
    """
    pass