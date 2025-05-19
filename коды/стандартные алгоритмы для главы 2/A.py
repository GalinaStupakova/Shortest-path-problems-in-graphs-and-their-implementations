import psutil
import snap
from scipy.sparse import lil_matrix
import time

# Загрузка графа
G = snap.LoadEdgeList(snap.PUNGraph, "graph_with_100001vertexbd.txt", 0, 1)
num_nodes = G.GetNodes()
positions = {}
with open("positions01.txt") as f:
    for line in f:
        node, x, y = map(int, line.strip().split())
        positions[int(node)] = (x, y)
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

def heuristic(u, v):
    u_id = index_to_node_id[u]
    v_id = index_to_node_id[v]
    x1, y1 = positions[u]
    x2, y2 = positions[v]
    return abs(x1 - x2) + abs(y1 - y2)

open_set = [start]
g_score = [inf] * n
g_score[start] = 0
visited = [False] * n

start_time = time.time()

while open_set:
    # Находим узел с минимальным f = g + h
    current = min(open_set, key=lambda u: g_score[u] + heuristic(u, end))
    if current == end:
        break

    open_set.remove(current)
    visited[current] = True

    for neighbor in matrix.rows[current]:
        if visited[neighbor]:
            continue
        tentative_g = g_score[current] + 1
        if tentative_g < g_score[neighbor]:
            g_score[neighbor] = tentative_g
            if neighbor not in open_set:
                open_set.append(neighbor)


end_time = time.time()

print(f"Время выполнения: {end_time - start_time:.2f} секунд")
print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")

