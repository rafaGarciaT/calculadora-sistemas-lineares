# Relatório: Teoria Matemática para Implementação da Calculadora de Sistemas Lineares

## 1. Introdução

Este relatório apresenta a fundamentação matemática necessária para implementar a calculadora de sistemas lineares do projeto. O método utilizado é a **Eliminação de Gauss** (Escalonamento), seguido da classificação do sistema (SPD, SPI ou SI) e da substituição retroativa para obter a solução.

---

## 2. Conceitos Fundamentais

### 2.1 Sistemas Lineares

Um sistema linear de **m** equações com **n** incógnitas tem a forma:

```
a₁₁x₁ + a₁₂x₂ + ... + a₁ₙxₙ = b₁
a₂₁x₁ + a₂₂x₂ + ... + a₂ₙxₙ = b₂
⋮
aₘ₁x₁ + aₘ₂x₂ + ... + aₘₙxₙ = bₘ
```

Onde:
- **aᵢⱼ** são os coeficientes das incógnitas
- **xⱼ** são as incógnitas
- **bᵢ** são os termos independentes

### 2.2 Representação Matricial

O sistema pode ser representado como uma **matriz aumentada**:

```
[a₁₁  a₁₂  ...  a₁ₙ | b₁]
[a₂₁  a₂₂  ...  a₂ₙ | b₂]
[⋮    ⋮    ...  ⋮   | ⋮ ]
[aₘ₁  aₘ₂  ...  aₘₙ | bₘ]
```

Esta representação facilita a aplicação de operações elementares.

### 2.3 Tipos de Sistemas

- **Sistema Determinado**: Possui uma única solução
- **Sistema Indeterminado**: Possui infinitas soluções
- **Sistema Impossível (Inconsistente)**: Não possui solução

---

## 3. Método de Eliminação de Gauss

### 3.1 Princípios Fundamentais

O método baseia-se em **operações elementares de linhas** que não alteram a solução do sistema:

1. **Trocar duas linhas**: Lᵢ ↔ Lⱼ
2. **Multiplicar uma linha por um escalar não-nulo**: Lᵢ → k·Lᵢ (k ≠ 0)
3. **Adicionar a uma linha uma múltipla de outra**: Lᵢ → Lᵢ + k·Lⱼ

### 3.2 Forma Escalonada

Uma matriz está em **forma escalonada** quando:

1. **Linhas nulas estão abaixo**: Todas as linhas com zeros ficam na base
2. **Primeiro elemento não-nulo (pivô)**: Em cada linha não-nula, o primeiro elemento não-nulo está à direita do pivô da linha anterior
3. **Estrutura de degraus**: Os pivôs formam um padrão diagonal descendente

**Exemplo de matriz escalonada:**
```
[1  2  3 | 5]
[0  4  5 | 6]
[0  0  7 | 8]
```

### 3.3 Forma Escalonada Reduzida (Gauss-Jordan)

Quando aplicamos operações adicionais para obter:

1. O pivô de cada linha é igual a 1
2. Todos os elementos acima e abaixo do pivô são zeros

**Exemplo:**
```
[1  0  0 | 5]
[0  1  0 | 6]
[0  0  1 | 8]
```

---

## 4. Algoritmo de Eliminação de Gauss

### 4.1 Etapas do Algoritmo

#### Fase 1: Escalonamento para Frente (Forward Elimination)

**Para cada coluna k (k = 1, 2, ..., n-1):**

1. **Localizar o Pivô**:
   - Encontrar a linha com o maior valor absoluto na coluna k (a partir da linha k)
   - Este é o **pivô parcial** - estratégia para melhorar estabilidade numérica

2. **Trocar Linhas** (se necessário):
   - Se o pivô não está na linha k, trocar as linhas

3. **Verificar Singularidade**:
   - Se o pivô é zero, a matriz é singular ou o sistema é indeterminado/impossível

4. **Eliminação**:
   - Para cada linha i (i > k):
     - Calcular o fator: mᵢₖ = aᵢₖ / aₖₖ
     - Para cada coluna j (j ≥ k):
       - aᵢⱼ ← aᵢⱼ - mᵢₖ · aₖⱼ
     - bᵢ ← bᵢ - mᵢₖ · bₖ

#### Fase 2: Substituição Retroativa (Back Substitution)

**Para cada linha k (k = n, n-1, ..., 1):**

1. xₖ ← (bₖ - Σ(aₖⱼ · xⱼ) para j > k) / aₖₖ

---

## 5. Exemplo Prático Completo

### 5.1 Sistema Original

```
2x + 3y + z = 11
x + 2y + z = 8
3x + y + 2z = 12
```

Matriz aumentada:
```
[2  3  1 | 11]
[1  2  1 | 8 ]
[3  1  2 | 12]
```

### 5.2 Escalonamento

**Passo 1**: Trocar L₁ e L₃ (pivô parcial - 3 > 2)
```
[3  1  2 | 12]
[1  2  1 | 8 ]
[2  3  1 | 11]
```

**Passo 2**: Eliminar x das linhas 2 e 3
- m₂₁ = 1/3: L₂ ← L₂ - (1/3)·L₁
- m₃₁ = 2/3: L₃ ← L₃ - (2/3)·L₁

```
[3   1        2      | 12    ]
[0   5/3      1/3    | 4     ]
[0   7/3     -1/3    | 3     ]
```

**Passo 3**: Eliminar y da linha 3
- m₃₂ = (7/3)/(5/3) = 7/5: L₃ ← L₃ - (7/5)·L₂

```
[3   1      2    | 12]
[0   5/3    1/3  | 4 ]
[0   0     -2/5  |-1 ]
```

### 5.3 Substituição Retroativa

De trás para frente:

1. -2/5 · z = -1 → **z = 5/2**
2. 5/3 · y + 1/3 · (5/2) = 4 → **y = 3/2**
3. 3 · x + 1 · (3/2) + 2 · (5/2) = 12 → **x = 2**

**Solução**: x = 2, y = 3/2, z = 5/2

---

## 6. Análise de Casos Especiais

### 6.1 Sistema Impossível

Quando durante o escalonamento aparece uma linha:
```
[0  0  0 | c] onde c ≠ 0
```

Isto implica uma contradição (0 = c), logo **não há solução**.

### 6.2 Sistema Indeterminado

Quando o número de equações não-nulas é menor que o número de incógnitas:
```
[1  2  3 | 5]
[0  0  0 | 0]
[0  0  0 | 0]
```

Há **infinitas soluções** (variáveis livres).

### 6.3 Matriz Singular

Quando o determinante é zero, a matriz não é invertível. Isto resulta em:
- Sistema impossível, ou
- Sistema indeterminado

---

## 7. Estabilidade Numérica

### 7.1 Pivô Parcial

Para evitar **erros de arredondamento**, usar o maior valor absoluto como pivô:

```python
# Encontrar máximo na coluna k
max_row = k
for i in range(k+1, n):
    if abs(matrix[i][k]) > abs(matrix[max_row][k]):
        max_row = i
# Trocar linhas
```

### 7.2 Número de Condicionamento

A estabilidade do sistema pode ser caracterizada pelo **número de condicionamento κ(A)**:
- κ(A) ≈ 1: Sistema bem-condicionado
- κ(A) >> 1: Sistema mal-condicionado (sensível a perturbações)

---

## 8. Complexidade Computacional

### 8.1 Análise de Tempo

- **Fase de Escalonamento**: O(n³)
  - n iterações (colunas)
  - Cada iteração processa até n linhas
  - Cada linha requer até n operações

- **Fase de Substituição**: O(n²)

- **Complexidade Total**: **O(n³)**

### 8.2 Análise de Espaço

- **Espaço da Matriz**: O(n·m)
- **Espaço de Trabalho**: O(n)

---

## 9. Validações Necessárias

Na implementação, considerar:

1. **Verificação de Entrada**:
   - Número de colunas = número de incógnitas
   - Número de linhas = número de equações
   - Matriz não vazia

2. **Detecção de Matriz Singular**:
   - Pivô zero em posição crítica
   - Determinante ≈ 0

3. **Precisão Numérica**:
   - Comparar com tolerância (ε = 1e-10)
   - Arredondar valores próximos a zero

4. **Verificação de Solução**:
   - Substituir a solução no sistema original
   - Verificar se Ax = b dentro de tolerância

---

## 10. Estrutura de Implementação em Python

### 10.1 Módulos do Projeto

```
src/
├── main.py            # Fluxo principal do programa
├── sistema.py         # Funções utilitárias para manipulação de matrizes
├── input_output.py    # Entrada e saída de dados (interação com o usuário)
├── escalonamento.py   # Algoritmo de Eliminação de Gauss
└── solver.py          # Classificação do sistema e substituição retroativa
```

### 10.2 Responsabilidades de Cada Módulo

**sistema.py** — Módulo utilitário (usado pelos demais):
- `criar_sistema(tamanho)`: cria a matriz aumentada (n x n+1) de zeros
- `copiar_sistema(sistema)`: cria uma cópia profunda da matriz
- `validar_sistema(sistema)`: valida o formato (n x n+1) e tipos numéricos
- `obter_numero_de_variaveis(sistema)`: retorna o número de variáveis (n)

**input_output.py** — Entrada e saída:
- `solicitar_tamanho_de_sistema()`: solicita o número de variáveis ao usuário
- `solicitar_sistema(tamanho)`: solicita os coeficientes e termos independentes
- `imprimir_sistema(sistema)`: exibe o sistema formatado no console
- `imprimir_resultado(resultado)`: exibe a solução ou mensagem de classificação

**escalonamento.py** — Eliminação de Gauss:
- `escalonar_sistema(sistema)`: aplica o escalonamento manualmente (sem numpy.linalg), retornando a matriz triangular superior

**solver.py** — Classificação e resolução:
- `classificar_sistema(sistema_escalonado)`: analisa a matriz escalonada e retorna "SPD", "SPI" ou "SI"
- `substituicao_retroativa(sistema_escalonado)`: resolve o sistema por substituição retroativa (apenas para SPD)
- `resolver(sistema_escalonado)`: orquestra a classificação e a resolução

### 10.3 Fluxo do Programa (main.py)

```
1. Solicitar tamanho do sistema          (input_output)
2. Solicitar coeficientes e termos       (input_output → sistema)
3. Imprimir sistema original             (input_output)
4. Escalonar o sistema                   (escalonamento → sistema)
5. Imprimir sistema escalonado           (input_output)
6. Classificar e resolver                (solver → sistema)
7. Imprimir resultado                    (input_output)
```

### 10.4 Dependências entre Módulos

```
main.py
  ├── input_output.py
  │     └── sistema.py  (criar_sistema, validar_sistema)
  ├── escalonamento.py
  │     └── sistema.py  (copiar_sistema, obter_numero_de_variaveis)
  └── solver.py
        └── sistema.py  (obter_numero_de_variaveis)
```

A biblioteca **numpy** é utilizada para manipulação de matrizes, mas o processo de escalonamento e resolução é implementado manualmente.

---

## 11. Referências Teóricas

- **Álgebra Linear Numérica**: O método de Eliminação de Gauss é um dos pilares da álgebra linear computacional
- **Estabilidade Numérica**: Golub & Van Loan (1996) - Matrix Computations
- **Sistemas Lineares**: Axelsson (1994) - Iterative Solution Methods for Linear Systems

---

## Conclusão

O método de Eliminação de Gauss é uma técnica fundamental e eficiente para resolver sistemas lineares. A implementação cuidadosa, considerando estabilidade numérica e casos especiais, resulta em uma calculadora robusta e confiável.

A decomposição do código em módulos específicos (`sistema.py`, `input_output.py`, `escalonamento.py` e `solver.py`) facilita o trabalho em equipe, a manutenção, os testes e a extensão futura.

