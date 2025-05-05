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

def bubble_sort(arr, optimize=True):

    # Operation counters
    comparisons = 0
    swaps = 0
    iterations = 0

    # Outer loop to iterate through the list n times
    for n in range(len(arr) - 1, 0, -1):
        iterations += 1
        
        # Initialize swapped to track if any swaps occur
        swapped = False  

        # Inner loop to compare adjacent elements
        for i in range(n):
            comparisons += 1
            if arr[i] > arr[i + 1]:
              
                # Swap elements if they are in the wrong order
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swaps += 1
                
                # Mark that a swap has occurred
                swapped = True
        
        # If no swaps occurred, the list is already sorted
        if (not swapped) and optimize:
            break
    
    return arr, {"comparisons": comparisons, "swaps": swaps, "iterations": iterations}

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
        

def newIntegerList(inp_size=None):
    type   = new_args.get('-t')

    if(type == None or (type != None and type not in ['ordered', 'random', 'fully_disordered'])):
        type = 'random'

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

    # Set-up variables
    arr = newIntegerList(inp_size)

    if(comparison): 
        # Create a new array position
        pre_arr = list(arr)

    print("\nUnsorted list is:")
    np_array = np.array(arr)
    print(np_array)

    start_time = time.perf_counter()
    arr, stats = bubble_sort(arr, optimize)
    stop_time = time.perf_counter()

    print("\nSorted list is:")
    np_array = np.array(arr)
    print(np_array)

    runtime = (stop_time - start_time)
    print("\n ===== // ==== // =====")

    print(optimizedText)

    print(f"\nRuntime: {(runtime * 1000):.4f} milliseconds ({runtime:.2f} sec)")
    print("Stats:", stats)

    runtime_chart.append(runtime)
    comparison_chart.append(stats.get('comparisons'))
    swaps_chart.append(stats.get('swaps'))
    iterations_chart.append(stats.get('iterations'))

    if(comparison):
        pre_np_array = np.array(pre_arr)
        print(pre_np_array)
        start_time_c = time.perf_counter()
        pre_arr, stats_c = bubble_sort(pre_arr, not optimize)
        stop_time_c = time.perf_counter()

        runtime_c = (stop_time_c - start_time_c)

        print("\n ===== // ===== // =====")

        print('Optimized' if not optimize else 'Non-Optimized')

        print(f"\nRuntime: {(runtime_c * 1000):.4f} milliseconds ({runtime_c:.2f} sec)")
        print("Stats:", stats_c)

        print("\n ===== // ===== // =====")

        print(f"\nRuntime diff: {((runtime - runtime_c) * 1000):.4f} milliseconds ({runtime - runtime_c:.2f} sec)")
        print("Stats diff:", {"comparisons": (stats.get('comparisons') - stats_c.get('comparisons')), "swaps": (stats.get('swaps') - stats_c.get('swaps')), "iterations": (stats.get('iterations') - stats_c.get('iterations'))})



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
fig.suptitle(f"Análise de Desempenho do Bubble Sort ({optimizedText}) - {type}", fontsize=16)

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
plt.savefig(f"{my_path}/results/{optimizedText}_{type}_bubble_sort_analise.png", dpi=300)
# Não chamamos plt.show() para evitar problemas com o display
# Os gráficos serão salvos como arquivos

# Gráfico log-log para análise de complexidade
plt.figure(figsize=(10, 6))
plt.loglog(input_size, runtime_chart, 'o-', label=f"Tempo de Execução (Bubble Sort - {optimizedText})", linewidth=2)
plt.loglog(input_size, [n**2 / 10**6 for n in input_size], '--', label='O(n²)', linewidth=2)
plt.loglog(input_size,  [n * np.log(n) / 18000 for n in input_size], '--', label='O(n log n)', linewidth=2)
plt.xlabel('Tamanho da Entrada (log)')
plt.ylabel('Tempo (log)')
plt.title(f"Análise de Complexidade do Bubble Sort ({optimizedText}) - {type}")
plt.legend()
plt.grid(True)
plt.savefig(f"{my_path}/results/{optimizedText}_{type}_bubble_sort_complexidade.png", dpi=300)
# Removido plt.show()

# Análise estatística
print(dados)
print("\nEstatísticas:")
print(dados.describe())

print("\nTodos os gráficos foram salvos com sucesso nos seguintes arquivos:")
print("1. bubble_sort_analise.png - Gráficos principais")
print("2. bubble_sort_complexidade.png - Análise de complexidade")