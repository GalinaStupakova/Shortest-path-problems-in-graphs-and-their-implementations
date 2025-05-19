import timeit
import psutil
import snap
from scipy.sparse import lil_matrix
from fibheap import makefheap, fheappop, Node 

code_to_test = '''
from scipy.sparse import lil_matrix
from fibheap import makefheap, fheappop, Node

# Загрузка графа
G = snap.LoadEdgeList(snap.PUNGraph, "facebook_combined.txt", 0, 1)
num_nodes = G.GetNodes()
n = num_nodes
inf = 1e8

node_id_to_index = {}
index = 0
for node in G.Nodes():
    node_id_to_index[node.GetId()] = index
    index += 1

# Матрица смежности
matrix = lil_matrix((num_nodes, num_nodes))
for EI in G.Edges():
    src_index = node_id_to_index[EI.GetSrcNId()]
    dst_index = node_id_to_index[EI.GetDstNId()]
    matrix[src_index, dst_index] = 1
    matrix[dst_index, src_index] = 1  

start = 99
end = 3999
visited = [False] * n
dist = [inf] * n
dist[start] = 0

heap = makefheap()
nodes = [None] * n

nodes[start] = Node((0, start))
heap.insert(nodes[start])

while heap.min is not None:
    current_distance, current_vertex = fheappop(heap)

    if visited[current_vertex]:
        continue

    visited[current_vertex] = True

    for neighbor_index in matrix.rows[current_vertex]:
        w = 1
        if not visited[neighbor_index]:
            distance = current_distance + w
            if distance < dist[neighbor_index]:
                dist[neighbor_index] = distance
                if nodes[neighbor_index] is None:
                    nodes[neighbor_index] = Node((distance, neighbor_index))
                    heap.insert(nodes[neighbor_index])
                else:
                    heap.decrease_key(nodes[neighbor_index], (distance, neighbor_index))

print('Расстояние от', start + 1, "до", end + 1, 'равно', dist[end])
print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")
'''

elapsed_time = timeit.timeit(stmt=code_to_test, number=1, globals=globals())
print(f"Время выполнения: {elapsed_time:.2f} сек")
