import time
import matplotlib.pyplot as plt
import random
inf = 1e8
def floyd_warshall(adj_matrix, n):
    dist = [row[:] for row in adj_matrix] 
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

def generate_adj_matrix(n, p):
    matrix = [[inf] * n for _ in range(n)]
    for i in range(n):
        matrix[i][i] = 0
        for j in range(i + 1, n):
            if random.random() < p:
                matrix[i][j] = matrix[j][i] = 1 
    return matrix

def measure_time_fw(n, p):
    matrix = generate_adj_matrix(n, p)
    start = time.time()
    floyd_warshall(matrix, n)
    return time.time() - start

# Диапазон n и p
n_values = list(range(1000, 5000, 500))  # Меньше, т.к. O(n^3)
p_values = [0.1, 0.5, 0.9]
results = {p: [] for p in p_values}

for p in p_values:
    for n in n_values:
        t = measure_time_fw(n, p)
        results[p].append(t)
        print(f"n = {n}, p = {p}, time = {t:.4f} сек")

# Построение графика
plt.figure(figsize=(10, 6))
for p in p_values:
    plt.plot(n_values, results[p], 'o-', label=f'p={p}')
    plt.text(n_values[0], results[p][0], f'{results[p][0]:.2f}с', ha='right', va='bottom')
    plt.text(n_values[-1], results[p][-1], f'{results[p][-1]:.2f}с', ha='left', va='top')

plt.xlabel('Число вершин (n)')
plt.ylabel('Время (сек)')
plt.title('алгоритм Флойда–Уоршелла')
plt.grid(True)
plt.legend()
plt.show()
