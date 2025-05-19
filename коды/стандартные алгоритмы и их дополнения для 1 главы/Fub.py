import fibheap

n = int(input())
weight = [list(map(int, input().split())) for _ in range(n)]
graph = [[] for _ in range(n)]
start = int(input()) - 1
inf = 1e8
visited = [False] * n
dist = [inf] * n
dist[start] = 0

# инициализация кучи
heap = fibheap.makefheap()
nodes = [None] * n  # Сохраняем узлы, чтобы обновлять значения

# Инициализация графа
for i in range(n):
    for j in range(n):
        if weight[i][j] != 0:
            graph[i].append((j, weight[i][j]))

nodes[start] = fibheap.Node((0, start))
heap.insert(nodes[start])

while heap.min is not None:
    current_distance, current_vertex = fibheap.fheappop(heap)

    if visited[current_vertex]:
        continue

    visited[current_vertex] = True

    for neighbor, w in graph[current_vertex]:
        if not visited[neighbor]:
            distance = current_distance + w
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                if nodes[neighbor] is None:
                    # Первый раз добавляем в кучу
                    nodes[neighbor] = fibheap.Node((distance, neighbor))
                    heap.insert(nodes[neighbor])
                else:
                    # Обновляем значение (decrease-key)
    
                    heap.decrease_key(nodes[neighbor], (distance, neighbor))

for i in range(n):
    print(f'Расстояние от {start + 1} до {i + 1} равно {dist[i]}')
