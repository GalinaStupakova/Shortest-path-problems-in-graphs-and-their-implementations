import snap
import time
import matplotlib.pyplot as plt
import random
inf = 1e8
def bellman_ford(Graph, start_node, n):
    dist = {node.GetId(): inf for node in Graph.Nodes()}
    dist[start_node] = 0

    for _ in range(n - 1):
        for edge in Graph.Edges():
            u = edge.GetSrcNId()
            v = edge.GetDstNId()
            if dist[u] + 1 < dist[v]:  # вес всех рёбер = 1
                dist[v] = dist[u] + 1
            if dist[v] + 1 < dist[u]:
                dist[u] = dist[v] + 1
    return dist

def measure_time_fixed_n(n, m):
    Graph = snap.GenRndGnm(snap.PUNGraph, n, m)
    start_time = time.time()
    bellman_ford(Graph, 0, n)
    return time.time() - start_time

# Параметры
n_fixed = 200
m_values = list(range(500, 19901, 500))
times = []

for m in m_values:
    t = measure_time_fixed_n(n_fixed, m)
    times.append(t)
    print(f"m = {m}, time = {t:.4f} сек")

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(m_values, times, 'o-', label=f'n = {n_fixed}')

# Подписи крайних точек
plt.text(m_values[0], times[0], f'{times[0]:.2f}с', ha='right', va='bottom')
plt.text(m_values[-1], times[-1], f'{times[-1]:.2f}с', ha='left', va='top')

plt.xlabel('Число рёбер (m)')
plt.ylabel('Время (сек)')
plt.title('Форд-Беллман: фиксированное количество вершин')
plt.grid(True)
plt.legend()
plt.show()
