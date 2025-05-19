import snap
import time
import matplotlib.pyplot as plt
inf = 1e8

def bellman_ford(graph, start, n):
    dist = {i: inf for i in range(n)}
    dist[start] = 0
    for _ in range(n - 1):
        for EI in graph.Edges():
            u, v = EI.GetSrcNId(), EI.GetDstNId()
            if dist[u] + 1 < dist[v]:
                dist[v] = dist[u] + 1
            if dist[v] + 1 < dist[u]:
                dist[u] = dist[v] + 1
    return dist

def measure_time(n, m):
    Graph = snap.GenRndGnm(snap.TUNGraph, n, m)
    start = time.time()
    bellman_ford(graph, 0, n)
    return time.time() - start

# Основной цикл
m = 4950
for n in range(100, 2001, 100):
    t = measure_time(n, m)
    print(f"n = {n}, время: {t:.4f} сек")

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(n_values, times, 'o-', label=f'm = {m_fixed}')

# Подписи к первой и последней точкам
plt.text(n_values[0], times[0], f'{times[0]:.2f}с', ha='right', va='bottom')
plt.text(n_values[-1], times[-1], f'{times[-1]:.2f}с', ha='left', va='top')

plt.xlabel('Число вершин (n)')
plt.ylabel('Время (сек)')
plt.title('Форд-Беллман: фиксированное количество рёбер')
plt.grid(True)
plt.legend()
plt.show()