import heapq

n = int(input())
weight = [list(map(int, input().split())) for _ in range(n)]
graph = [[] for _ in range(n)]
start = int(input()) - 1
inf = 1e8
visited = [False]*n
dist = [inf]*n
dist[start] = 0


vertex_heap = [(0, start)]


for i in range(n):
    for j in range(n):
        if weight[i][j] != 0:
            graph[i].append((j, weight[i][j]))


while vertex_heap:

    current_distance, current_vertex = heapq.heappop(vertex_heap)


    if current_distance > dist[current_vertex]:
        continue


    for neighbor, weight in graph[current_vertex]:
        if not visited[neighbor]:
            distance = current_distance + weight

      
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(vertex_heap, (distance, neighbor))

    visited[current_vertex] = True

for i in range(len(dist)):
    print('Расстояние от', start + 1, "до", i +1, 'равно', dist[i])