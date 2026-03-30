from .escalonamento import escalonar_sistema
from .solver import classificar_sistema, substituicao_retroativa, resolver
from .sistema import (
    criar_sistema,
    copiar_sistema,
    validar_sistema,
    obter_numero_de_variaveis,
)
from .input_output import (
    solicitar_tamanho_de_sistema,
    solicitar_sistema,
    imprimir_sistema,
    imprimir_resultado,
)

__all__ = [
    "escalonar_sistema",
    "classificar_sistema",
    "substituicao_retroativa",
    "resolver",
    "criar_sistema",
    "copiar_sistema",
    "validar_sistema",
    "obter_numero_de_variaveis",

    "solicitar_tamanho_de_sistema",
    "solicitar_sistema",
    "imprimir_sistema",
    "imprimir_resultado",
]

__version__ = "0.1.0"
