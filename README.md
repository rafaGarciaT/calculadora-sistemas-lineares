# Calculadora de Sistemas Lineares
Calculadora Python para resolver sistemas lineares utilizando o método de Eliminação de Gauss (ou, escalonamento). 
O projeto implementa a transformação de matrizes aumentadas em forma triangular superior e classifica sistemas como determinados (SPD), indeterminados (SPI) ou impossíveis (SI).

## Execução

```bash
python -m src.main
```

Ou copie o código em monolito.py e cole em um compilador online.

## Estrutura do Projeto

```
calculadora-sistemas-lineares/
├── src/
│   ├── __init__.py          # Exportações dos módulos
│   ├── main.py              # Ponto de entrada da aplicação
│   ├── input_output.py      # Entrada de dados e formatação de saída
│   ├── sistema.py           # Operações com matrizes
│   ├── escalonamento.py     # Eliminação de Gauss
│   └── solver.py            # Classificação e resolução do sistema
├── tests/                   # Testes unitários
├── notebooks/               # Jupyter notebooks explicativos
├── requirements.txt         # Dependências do projeto
└── README.md              
```

## Documentação Adicional
- `notebooks/` - Notebooks Jupyter com explicações detalhadas

## 👥 Equipe Original do Projeto

- Ana Carolina Miranda
- Caio Danjo
- José Guilherme
- Livia Lana
- Rafael Garcia


| Etapa/Módulo  | Responsável    |
|---------------|----------------|
| Input/Output  | Ana Carolina   |
| Sistema       | Caio Danjo     |
| Escalonamento | José Guilherme |
| Solver        | Lívia Lana     |
| Main          | Rafael Garcia  |
| Notebooks     | Rafael Garcia  |
