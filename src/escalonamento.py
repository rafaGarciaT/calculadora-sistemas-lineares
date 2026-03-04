import numpy as np
from src.sistema import copiar_sistema, obter_numero_de_variaveis


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
    pass