import numpy as np
from sistema import copiar_sistema, obter_numero_de_variaveis


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
    mat = copiar_sistema(sistema)
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