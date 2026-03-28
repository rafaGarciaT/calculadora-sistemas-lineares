# calculadora-sistemas-lineares

Este projeto implementa uma calculadora em Python que resolve sistemas lineares utilizando o método de escalonamento (Eliminação de Gauss).

## Integrantes 
- Ana Carolina Miranda
- Caio Danjo
- José Guilherme
- Livia Lana
- Rafael Garcia


## Estrutura do Código A Ser Desenvolvido

```
calculadora-sistemas-lineares/
│
├── src/
│   ├── main.py
│   ├── input_output.py
│   ├── sistema.py
│   ├── escalonamento.py
│   └── solver.py
│
├── tests/
│
├── docs/
│
├── notebooks/      # Notebooks explicativos
│
├── exemplos/       # Exemplos para usarmos no vídeo
│
├── requirements.txt
└── README.md

```

## Etapas do código - divisão

| Etapa                                   | Responsável            |
|-----------------------------------------|------------------------|
| Input/Output                            |      Ana Carolina      |
| Sistema                                 |       Caio Danjo       |
| Escalonamento                           |          ...           |
| Solver                                  |          ...           |


## O Que Cada Branch Deve Conter

Cada branch deve mexer com um módulo específico do projeto:
- **input_output.py**: solicita o tamanho do sistema, os coeficientes e os termos independentes. Imprime o sistema formatado, escalonado, e a solução.
- **escalonamento.py**: realiza o processo de escalonamento e retorna a matriz escalonada.
- **solver.py**: analisa a matriz escalonada, determina o tipo de sistema (SPD, SPI, SI) e resolve o sistema por substituição se possível.
- **sistema.py**: realiza operações auxiliares relacionada a matrizes.

A main já possui o fluxo do programa, e os módulos já tem funções vazias com parâmetros definidos. O trabalho de cada branch é implementar essas funções (apenas substituindo o pass, não apague os docstrings, eles definem o que exatamente a função deve ter).
Para equilibrar as tarefas, cada integrante escolhe um módulo para implementar.

## Bibliotecas

Utilizaremos o numpy para a manipulação de matrizes, mas o processo de escalonamento e resolução deve ser implementado manualmente.

## Teoria

Se você não lembra muito o método de escalonamento, em docs/ eu deixei alguns materiais que pode ajudar:
- um .md gerado que explica o conteúdo
- dois PDFs das minhas anotações que fiz a partir da gravação da aula, um sobre o processo de escalonamento e outro sobre os tipos de sistemas lineares.

## Vídeo

Vamos cuidar disso depois que o código estiver pronto.
