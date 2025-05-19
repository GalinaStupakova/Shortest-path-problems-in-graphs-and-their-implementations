import psutil
import snap
from scipy.sparse import lil_matrix
import time

# Загрузка графа
G = snap.LoadEdgeList(snap.PUNGraph, "graph_with_10000vertexbd.txt", 0, 1)
num_nodes = G.GetNodes()
inf = 1e8

# Сопоставление ID узлов и индексов матрицы
node_id_to_index = {}
index_to_node_id = {}
index = 0
for node in G.Nodes():
    nid = node.GetId()
    node_id_to_index[nid] = index
    index_to_node_id[index] = nid
    index += 1

# Построение разреженной матрицы смежности
n = num_nodes
matrix = lil_matrix((n, n))
for EI in G.Edges():
    src = node_id_to_index[EI.GetSrcNId()]
    dst = node_id_to_index[EI.GetDstNId()]
    matrix[src, dst] = 1
    matrix[dst, src] = 1 

start = 999
end = 8999

# Инициализация расстояний и флагов посещения
dist_start = [inf] * n
dist_end = [inf] * n
visited_start = [False] * n
visited_end = [False] * n

dist_start[start] = 0
dist_end[end] = 0

start_time = time.time()

def get_min_index(dist, visited):
    min_val = float('inf')
    min_index = -1
    for i in range(len(dist)):
        if not visited[i] and dist[i] < min_val:
            min_val = dist[i]
            min_index = i
    return min_index

# Двунаправленный поиск
step = 0
flag = False
while not flag:
    u = get_min_index(dist_start, visited_start)
    v = get_min_index(dist_end, visited_end)

    if u == -1 and v == -1:
        break

    if u != -1:
        visited_start[u] = True
        for neighbor in range(n):
            if matrix[u, neighbor] > 0 and not visited_start[neighbor]:
                dist_start[neighbor] = min(dist_start[neighbor], dist_start[u] + matrix[u, neighbor])

    if v != -1:
        visited_end[v] = True
        for neighbor in range(n):
            if matrix[neighbor, v] > 0 and not visited_end[neighbor]:
                dist_end[neighbor] = min(dist_end[neighbor], dist_end[v] + matrix[neighbor, v])

    # Проверка на встречу двух сторон
    for i in range(n):
        if visited_start[i] and visited_end[i]:
            total = dist_start[i] + dist_end[i]
            flag = True
            break


shortest = inf
for u in range(n):
    if visited_start[u]:
        for v in range(n):
            if visited_end[v] and matrix[u, v] > 0:
                total = dist_start[u] + matrix[u, v] + dist_end[v]
                if total < shortest:
                    shortest = total
end_time = time.time()

print("Расстояние от вершины", start + 1 "до", end + 1, "равно", shortest)
print(f"Время выполнения: {end_time - start_time:.2f} секунд")
print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")













