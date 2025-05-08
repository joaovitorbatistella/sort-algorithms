import matplotlib

# Definir o backend para 'Agg' (não interativo) para evitar problemas com GTK
matplotlib.use('Agg')

import os
my_path = os.path.dirname(os.path.abspath(__file__))

import sys
import time
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def heapify(arr, n, i, counters):
    counters['iterations'] += 1
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    counters['comparisons'] += 1
    if l < n: 
        counters['comparisons'] += 1
        if arr[i] < arr[l]:
            largest = l

    # See if right child of root exists and is
    # greater than root
    counters['comparisons'] += 1
    if r < n:
        counters['comparisons'] += 1
        if arr[largest] < arr[r]:
            largest = r

    # Change root, if needed
    counters['comparisons'] += 1
    if largest != i:
        counters['swaps'] += 1
        (arr[i], arr[largest]) = (arr[largest], arr[i])  # swap

        # Heapify the root.
        heapify(arr, n, largest, counters)


# The main function to sort an array of given size
def heapSort(arr):
    # Operation counters
    counters = {
        'comparisons': 0,
        'swaps': 0,
        'iterations': 0
    }

    n = len(arr)

    # Build a maxheap.
    # Since last parent will be at (n//2) we can start at that location.
    for i in range(n // 2, -1, -1):
        counters['iterations'] += 1
        heapify(arr, n, i, counters)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        counters['iterations'] += 1

        (arr[i], arr[0]) = (arr[0], arr[i])  # swap
        counters['swaps'] += 1

        heapify(arr, i, 0, counters)

    return arr, counters 

def remove_min_max(data):
    if not data:
        return []

    if len(data) < 3:
        return []
    
    result = data.copy()
    
    min_val = min(result)
    result.remove(min_val)

    max_val = max(result)
    result.remove(max_val)
    
    return result

def average_list(list1):
    if not list1 or len(list1) == 0:
        return 0
    
    if len(list1) >= 5:
        list1 = remove_min_max(list1)

    return sum(list1) / len(list1)

def createFullyDisorderedList(l_size):
    fully_disordered_arr = list()

    for number in range(l_size, 0, -1):
        fully_disordered_arr.append(number)

    return fully_disordered_arr

def createOrderedList(l_size):
    ordered_arr = list()

    for number in range(1, l_size+1):
        ordered_arr.append(number)

    return ordered_arr
        

def newIntegerList(inp_size=None, type='random'):
    if(type == 'random'):
        return np.random.randint(1, inp_size, inp_size)
    elif(type == 'ordered'):
        return createOrderedList(inp_size)
    elif(type == 'fully_disordered'):
        return createFullyDisorderedList(inp_size)
    else:
        print(f"Type {type} is undefined")
        return []


# Set-up chart variables
runtime_chart    = list()
comparison_chart = list()
swaps_chart      = list()
iterations_chart = list()

# Read  arguments
args = sys.argv
args.pop(0)

new_args = dict()
for (i, value) in enumerate(args):
    if(i%2 != 0):
        continue
    
    new_args[value] = args[i+1]

# Read type setting (Default: 'random')
type   = new_args.get('-t')
if(type == None or (type != None and type not in ['ordered', 'random', 'fully_disordered'])):
    type = 'random'

# Read optimize setting (Default: True)
optimize = new_args.get('-o')
if(optimize == None or (optimize != None and optimize not in ['true', 'True', 'false', 'False'])):
    optimize = 'True'

# Read comparison mode (Default: False)
comparison = new_args.get('-c')
if(comparison == None or (comparison != None and comparison not in ['true', 'True', 'false', 'False'])):
    comparison = 'False'
comparison = eval(comparison.capitalize())

# If comparison mode is enabled, first run with optimize disabled
if(comparison):
    optimize = 'False'

optimize = eval(optimize.capitalize())

optimizedText = 'Optimized' if optimize else 'Non-Optimized'

size = new_args.get('-s')
if(size == None):
    size = '10, 100, 1000, 10000'

size = str(size).split(",")

input_size = [int(num_str) for num_str in size]

for inp_size in input_size:
    print(f"\n\n\t\t ===== // == Input size ({inp_size}) == // =====")

    type   = new_args.get('-t')

    if(type == None or (type != None and type not in ['ordered', 'random', 'fully_disordered'])):
        type = 'random'

    tries = 1
    if(type == 'random'):
        tries = 3

    runtime_range    = list()
    comparison_range = list()
    swaps_range      = list()
    iterations_range = list()
    
    for i in range(tries):
        # Set-up variables
        arr = newIntegerList(inp_size, type)
        if(comparison): 
            # Create a new array position
            pre_arr = list(arr)

        print("\nUnsorted list is:")
        np_array = np.array(arr)
        print(np_array)

        start_time = time.perf_counter()
        arr, stats = heapSort(arr)
        stop_time = time.perf_counter()

        print("\nSorted list is:")
        np_array = np.array(arr)
        print(np_array)

        runtime = (stop_time - start_time)
        print("\n ===== // ==== // =====")

        print(optimizedText)

        print(f"\nRuntime: {(runtime * 1000):.4f} milliseconds ({runtime:.2f} sec)")
        print("Stats:", stats)

        print("runtime: ", runtime)

        runtime_range.append(runtime)
        comparison_range.append(stats.get('comparisons'))
        swaps_range.append(stats.get('swaps'))
        iterations_range.append(stats.get('iterations'))

        if(comparison):
            pre_np_array = np.array(pre_arr)
            print(pre_np_array)
            start_time_c = time.perf_counter()
            pre_arr, stats_c = heapSort(pre_arr)
            stop_time_c = time.perf_counter()

            runtime_c = (stop_time_c - start_time_c)

            print("\n ===== // ===== // =====")

            print('Optimized' if not optimize else 'Non-Optimized')

            print(f"\nRuntime: {(runtime_c * 1000):.4f} milliseconds ({runtime_c:.2f} sec)")
            print("Stats:", stats_c)

            print("\n ===== // ===== // =====")

            print(f"\nRuntime diff: {((runtime - runtime_c) * 1000):.4f} milliseconds ({runtime - runtime_c:.2f} sec)")
            print("Stats diff:", {"comparisons": (stats.get('comparisons') - stats_c.get('comparisons')), "swaps": (stats.get('swaps') - stats_c.get('swaps')), "iterations": (stats.get('iterations') - stats_c.get('iterations'))})

    runtime_chart.append(average_list(runtime_range))
    comparison_chart.append(average_list(comparison_range))
    swaps_chart.append(average_list(swaps_range))
    iterations_chart.append(average_list(iterations_range))

# Configurando o estilo dos gráficos
plt.style.use('seaborn-v0_8-darkgrid')
sns.set(font_scale=1.2)

# Criando um DataFrame para facilitar a análise
dados = pd.DataFrame({
    'Tamanho da Entrada': input_size,
    'Tempo de Execução (s)': runtime_chart,
    'Comparações': comparison_chart,
    'Swaps': swaps_chart,
    'Iterações': iterations_chart
})

# Configurando o layout do matplotlib
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle(F"Análise de Desempenho do Heap Sort - {type}", fontsize=16)

# 1. Gráfico de Tempo de Execução
axes[0, 0].plot(input_size, runtime_chart, 'o-', color='blue', linewidth=2, markersize=8)
axes[0, 0].set_title('Tempo de Execução')
axes[0, 0].set_xlabel('Tamanho da Entrada')
axes[0, 0].set_ylabel('Tempo (segundos)')
axes[0, 0].grid(True)

# 2. Gráfico de Comparações
axes[0, 1].plot(input_size, comparison_chart, 'o-', color='red', linewidth=2, markersize=8)
axes[0, 1].set_title('Número de Comparações')
axes[0, 1].set_xlabel('Tamanho da Entrada')
axes[0, 1].set_ylabel('Comparações')
axes[0, 1].grid(True)

# 3. Gráfico de Swaps
axes[1, 0].plot(input_size, swaps_chart, 'o-', color='green', linewidth=2, markersize=8)
axes[1, 0].set_title('Número de Swaps')
axes[1, 0].set_xlabel('Tamanho da Entrada')
axes[1, 0].set_ylabel('Swaps')
axes[1, 0].grid(True)

# 4. Gráfico de Iterações
axes[1, 1].plot(input_size, iterations_chart, 'o-', color='purple', linewidth=2, markersize=8)
axes[1, 1].set_title('Número de Iterações')
axes[1, 1].set_xlabel('Tamanho da Entrada')
axes[1, 1].set_ylabel('Iterações')
axes[1, 1].grid(True)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig(f"{my_path}/results/{optimizedText}_{type}_heap_sort_analise.png", dpi=300)
# Não chamamos plt.show() para evitar problemas com o display
# Os gráficos serão salvos como arquivos

# Gráfico log-log para análise de complexidade
plt.figure(figsize=(10, 6))
plt.loglog(input_size, runtime_chart, 'o-', label='Tempo de Execução (Heap Sort)', linewidth=2)
plt.loglog(input_size, [n**2 / 10**6 for n in input_size], '--', label='O(n²)', linewidth=2)
plt.loglog(input_size,  [n * np.log(n) / 18000 for n in input_size], '--', label='O(n log n)', linewidth=2)
plt.xlabel('Tamanho da Entrada (log)')
plt.ylabel('Tempo (log)')
plt.title(f"Análise de Complexidade do Heap Sort - {type}")
plt.legend()
plt.grid(True)
plt.savefig(f"{my_path}/results/{optimizedText}_{type}_heap_sort_complexidade.png", dpi=300)
# Removido plt.show()

# Análise estatística
print(dados)
print("\nEstatísticas:")
print(dados.describe())

print("\nTodos os gráficos foram salvos com sucesso nos seguintes arquivos:")
print("1. bubble_sort_analise.png - Gráficos principais")
print("2. bubble_sort_complexidade.png - Análise de complexidade")