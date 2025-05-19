#тут с принтами

import timeit 
code_to_test = '''
import psutil
import snap
from scipy.sparse import lil_matrix

G = snap.LoadEdgeList(snap.PUNGraph, "roadNet-PA.txt", 0, 1)
num_nodes = G.GetNodes()
n = num_nodes

node_id_to_index = {}
index = 0
for node in G.Nodes():
    node_id_to_index[node.GetId()] = index
    index += 1


matrix = lil_matrix((num_nodes, num_nodes))


for EI in G.Edges():
    src_index = node_id_to_index[EI.GetSrcNId()]
    dst_index = node_id_to_index[EI.GetDstNId()]
    matrix[src_index, dst_index] = 1
    matrix[dst_index, src_index] = 1

start = 1
end = 1088
inf = 1e8
visited = [False] * n
dist = [inf] * n
dist[start] = 0

def gofrom():
    index = 0
    distmin = inf
    for i in range(n):
        if dist[i] < distmin and not visited[i]:
            distmin = dist[i]
            index = i
    return index

step = 0
while False in visited:
    u = gofrom()
    if u == end:
        break
    for v in range(num_nodes):
        if matrix[u, v] != 0 and not visited[v]:
            dist[v] = min(dist[v], dist[u] + matrix[u, v])
    visited[u] = True
    step += 1

print('Расстояние от', start + 1, "до", end + 1, 'равно', dist[end])
print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")
'''
elapsed_time = timeit.timeit(code_to_test, number=1)/1
print(elapsed_time)