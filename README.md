# 📊 Análise de Desempenho do Algoritmo Bubble Sort

Este projeto realiza uma análise de desempenho dos algoritmos de ordenação **Bubble Sort** e **Heap Sort**, podendo comparar sua versão otimizada e não otimizada em diferentes tamanhos de entrada para Bubble Sort. Os dados de execução são coletados e visualizados por meio de gráficos gerados automaticamente.

---

## 📌 Funcionalidades

- Implementação do algoritmo **Bubble Sort** com e sem otimização.
- Implementação do algoritmo **Heap Sort**.
- Suporte a diferentes tipos de listas:
  - Ordenada (`ordered`)
  - Aleatória (`random`)
  - Totalmente desordenada (`fully_disordered`)
- Coleta de métricas:
  - Tempo de execução
  - Número de comparações
  - Número de trocas (swaps)
  - Número de iterações
- Geração de gráficos salvos em arquivos:
  - Desempenho geral
  - Comparação de complexidade computacional

---

## ⚙️ Requisitos

- Python 3
- Bibliotecas:
  ```bash
  pip install numpy pandas matplotlib seaborn
  ```

---

## 🚀 Execução

Execute o script via terminal com os seguintes parâmetros:

```bash
python bubble_sort_analysis.py -s "10,100,1000" -t random -o true -c false
```

### Parâmetros

| Parâmetro | Descrição | Valores possíveis | Padrão |
|----------|-----------|-------------------|--------|
| `-s`     | Tamanhos das listas de entrada | Ex: `10,100,1000` | `10,100,1000,10000` |
| `-t`     | Tipo da lista | `random`, `ordered`, `fully_disordered` | `random` |
| `-o`     | Otimizar Bubble Sort? | `true`, `false` | `true` |
| `-c`     | Modo comparação entre otimizado e não otimizado (Apenas para **Bubble Sort**) | `true`, `false` | `false` |

**NOTE:** Se usar o modo de comparação, a saída gráfica será sempre do algoritmo não otimizado

---

## 🧠 Principais Funções

### `bubble_sort(arr, optimize=True)`
Implementa o algoritmo Bubble Sort. Se `optimize=True`, encerra a ordenação cedo se não houver trocas.

###  `heapSort(arr)`
Implementa o algoritmo Heap Sort.

**Retorna:**
- Lista ordenada
- Dicionário com estatísticas de execução: comparações, trocas e iterações.

---

## 📈 Gráficos Gerados

1. **Gráficos de desempenho**:  
   Salvo como: `results/Optimized_random_bubble_sort_analise.png`  
   Contém:
   - Tempo de execução
   - Comparações
   - Swaps
   - Iterações

2. **Gráfico de complexidade (log-log)**:  
   Salvo como: `results/Optimized_random_bubble_sort_complexidade.png`  
   Exibe:
   - Curva real de tempo de execução
   - Curva teórica O(n²)
   - Curva teórica O(n log n)

---

## 📊 Exemplo de saída no console

```text
         ===== // == Input size (100) == // =====
Unsorted list is:
[25  8 90  ...]
Sorted list is:
[ 1  2  3  ...]
Runtime: 3.4567 milliseconds (0.00 sec)
Stats: {'comparisons': 4950, 'swaps': 2450, 'iterations': 99}

Estatísticas:
       Tamanho da Entrada  Tempo de Execução (s)  Comparações  Swaps  Iterações
count                  4.0                4.000000     4.000000    4.0    4.000000
mean                2777.5                0.024000  160000.000000  ... ...
```

---

## 🗂 Estrutura de Arquivos

```
bubble_sort_analysis.py
results/
├── Optimized_random_bubble_sort_analise.png
└── Optimized_random_bubble_sort_complexidade.png
```

---

## 🧪 Análise Estatística

O script imprime uma análise estatística via `pandas.describe()`, mostrando média, desvio padrão e outros indicadores de:

- Tempo de execução
- Comparações
- Swaps
- Iterações

---

## 📤 Observações

- O backend gráfico utilizado é `Agg`, ideal para ambientes sem interface gráfica.
- Os gráficos são **salvos automaticamente** na pasta `results/`.
- A função `plt.show()` foi propositalmente omitida para evitar problemas em ambientes sem display.

---

## 📌 Referência de Complexidade

### Bubble Sort
- Pior caso: **O(n²)**
- Melhor caso (lista ordenada com otimização): **O(n)**

### Heap Sort
- Pior caso: **O(n log n)**
- Melhor caso (lista ordenada com otimização): **O(n log n)**