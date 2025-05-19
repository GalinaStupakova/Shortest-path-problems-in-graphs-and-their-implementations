import timeit

code_to_test = '''
import psutil
import snap
from scipy.sparse import lil_matrix

# Загрузка графа
G = snap.LoadEdgeList(snap.PNGraph, "Wiki-Vote.txt", 0, 1)
num_nodes = G.GetNodes()
inf = 1e8

# Создание отображения: Node ID → индекс
node_id_to_index = {}
index_to_node_id = {}
index = 0
for node in G.Nodes():
    nid = node.GetId()
    node_id_to_index[nid] = index
    index_to_node_id[index] = nid
    index += 1

n = num_nodes
# Матрица смежности
matrix = lil_matrix((n, n))

# Заполняем матрицу
for EI in G.Edges():
    src = node_id_to_index[EI.GetSrcNId()]
    dst = node_id_to_index[EI.GetDstNId()]
    matrix[src, dst] = 1
    matrix[dst, src] = 1 

# Выбираем начальные и конечные вершины
start = 99
end = 4999

# Инициализация расстояний и посещённости
dist_start = [inf] * n
dist_end = [inf] * n
dist_start[start] = 0
dist_end[end] = 0

visited_start = [False] * n
visited_end = [False] * n

# Поиск минимальной непосещённой вершины
def get_min_index(dist, visited):
    index = -1
    min_dist = inf
    for i in range(n):
        if dist[i] < min_dist and not visited[i]:
            min_dist = dist[i]
            index = i
    return index

# Основной цикл двунаправленного поиска
step = 0
flag = False
while flag == False:
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
                    # Проверяем, встретились ли две стороны (если вершина посещена с обеих сторон)
    for i in range(n):
        if visited_start[i] and visited_end[i]:
            total = dist_start[i] + dist_end[i]
            flag = True
            break

    step += 1

# Перебираем все пары, чтобы найти кратчайший путь
shortest = inf
for u in range(n):
    if visited_start[u]:
        for v in range(n):
            if visited_end[v] and matrix[u, v] > 0:
                total = dist_start[u] + matrix[u, v] + dist_end[v]
                if total < shortest:
                    shortest = total

print("Расстояние от вершины", start + 1 "до", end + 1, "равно", shortest)
print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")
#'''

elapsed_time = timeit.timeit(code_to_test, number=1)/1
print(elapsed_time)
