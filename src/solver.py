import numpy as np
from src.sistema import obter_numero_de_variaveis

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
        return "Sistema Possível Indeterminado (infinitas soluções)"
    else:
        return "Sistema Impossível (sem solução)"