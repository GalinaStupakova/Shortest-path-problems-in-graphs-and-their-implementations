import snap
import heapq
from scipy.sparse import lil_matrix
import time
import psutil

# Load the graph
G = snap.LoadEdgeList(snap.PUNGraph, "roadNet-PA.txt", 0, 1)
num_nodes = G.GetNodes()
n = num_nodes

# Create a mapping of node IDs to indices
node_id_to_index = {}
index = 0
for node in G.Nodes():
    node_id_to_index[node.GetId()] = index
    index += 1

# Create the adjacency matrix
matrix = lil_matrix((num_nodes, num_nodes))

# Populate the adjacency matrix
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

vertex_heap = [(0, start)]
start_time = time.time()

while vertex_heap:
    current_distance, current_vertex = heapq.heappop(vertex_heap)

    # Останавливаемся, если достигли конечной вершины
    if current_vertex == end:
        break

    if current_distance > dist[current_vertex]:
        continue

    for neighbor in range(num_nodes):
        if matrix[current_vertex, neighbor] != 0 and not visited[neighbor]:
            distance = current_distance + matrix[current_vertex, neighbor]
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(vertex_heap, (distance, neighbor))

    visited[current_vertex] = True

end_time = time.time()

print('Расстояние от', start + 1, "до", end + 1, 'равно', dist[end])
print(f"Время выполнения: {end_time - start_time:.2f} секунд")
print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")
