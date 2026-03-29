import numpy as np


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
    pass

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
    pass

def obter_numero_de_variaveis(sistema: np.ndarray) -> int:
    """
    Retorna o número de variáveis do sistema linear, que corresponde
    ao número de linhas da matriz aumentada.

    Args:
        sistema: matriz aumentada (n x n+1).

    Returns:
        int: número de variáveis (n).
    """
    return sistema.shape[0]