from src import escalonar_sistema, solicitar_tamanho_de_sistema, solicitar_sistema, imprimir_sistema, imprimir_resultado, resolver


def main():
    tamanho_sistema = solicitar_tamanho_de_sistema()
    sistema = solicitar_sistema(tamanho_sistema)
    imprimir_sistema(sistema)

    sistema_escalonado = escalonar_sistema(sistema)
    imprimir_sistema(sistema_escalonado)

    resultado = resolver(sistema_escalonado)
    imprimir_resultado(resultado)


if __name__ == "__main__":
    main()
