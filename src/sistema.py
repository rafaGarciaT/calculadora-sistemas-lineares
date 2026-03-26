import numpy as np


def criar_sistema(tamanho: int) -> np.ndarray:
    if tamanho <= 0 or tamanho > 10:
        raise ValueError("O tamanho deve estar entre 1 e 10.")
        
    return np.zeros((tamanho, tamanho + 1), dtype=float)

def copiar_sistema(sistema: np.ndarray) -> np.ndarray:
    return np.copy(sistema)

def validar_sistema(sistema: np.ndarray) -> bool:
    #Verifica se é numpy array
    if not isinstance(sistema, np.ndarray):
        return False
    
    #Verifica se é 2D
    if sistema.ndim != 2:
        return False
    
    linhas, colunas = sistema.shape

    #Verifica formato n x (n+1)
    if colunas != linhas + 1:
        return False
    
    #Verifica se todos são números
    try:
        sistema.astype(float)
    except (ValueError, TypeError):
        return False
    
    return True

def obter_numero_de_variaveis(sistema: np.ndarray) -> int:
    if not validar_sistema(sistema):
        raise ValueError("Sistema inválido.")
    
    return sistema.shape[0]