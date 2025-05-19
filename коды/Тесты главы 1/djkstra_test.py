import snap
import time
import matplotlib.pyplot as plt
import random
inf = 1e8
def dijkstra(weight, start):
    n = len(weight)
    visited = [False]*n
    dist = [INF]*n
    dist[start] = 0

    def gofrom():
        index = 0
        distmin = INF
        for i in range(n):
            if dist[i] < distmin and not visited[i]:
                distmin = dist[i]
                index = i
        return index

    while False in visited:
        u = gofrom()
        for v in range(n):
            if weight[u][v] != 0 and not visited[v]:
                dist[v] = min(dist[v], dist[u] + weight[u][v])
        visited[u] = True

    return dist

def measure_time(n, p):
    Graph = snap.TUNGraph.New()
    for i in range(n):
        Graph.AddNode(i)

    for u in range(n):
        for v in range(u + 1, n):
            if random.random() < p:
                Graph.AddEdge(u, v)
        
        start_time = time.time()
    weight = [[0]*n for _ in range(n)]
    for EI in Graph.Edges():
        u, v = EI.GetSrcNId(), EI.GetDstNId()
        weight[u][v] = 1
        weight[v][u] = 1 

    start_time = time.time()
    dijkstra(weight, 0)
    return time.time() - start_time

# Уменьшаем диапазон для теста
n_values = list(range(1000, 10001, 500))  # Тестируем на малых графах сначала
p_values = [0.1, 0.5, 0.9]
results = {p: [] for p in p_values}

print("Начинаем эксперимент...")
for p in p_values:
    for n in n_values:
        t = measure_time(n, p)
        results[p].append(t)
        print(f"n = {n}, p = {p}, время: {t:.4f} сек")

plt.figure(figsize=(10, 6))
for p in p_values:
    line, = plt.plot(n_values, results[p], 'o-', label=f'p={p}')
    
    # Подписи для первой и последней точек
    plt.text(n_values[0], results[p][0], f'{results[p][0]:.2f}с', 
             ha='right', va='bottom')
    plt.text(n_values[-1], results[p][-1], f'{results[p][-1]:.2f}с',
             ha='left', va='top')

plt.xlabel('Число вершин (n)')
plt.ylabel('Время (сек)')
plt.title('алгоритм Дейкстры')
plt.grid(True)
plt.legend()
plt.show()