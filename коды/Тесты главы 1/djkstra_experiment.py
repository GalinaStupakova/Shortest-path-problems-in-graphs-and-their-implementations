import time
import psutil

# Параметры
filename = "graph_with_500vertex.txt"  # ваш файл с графом
n = 1000                    # количество вершин
start = 500                 # начальная вершина
end = 700                   # конечная вершина
inf = float('inf')

# Загрузка графа

weight = [[inf] * n for _ in range(n)]
for i in range(n):
    weight[i][i] = 0

with open(filename) as f:
    for line in f:
        u, v, w = map(int, line.strip().split())
        weight[u][v] = w
        weight[v][u] = w 

# Инициализация
visited = [False] * n
dist = [inf] * n
dist[start] = 0


start_time = time.time()

def find_min_distance_vertex():
    min_dist = inf
    min_index = -1
    for i in range(n):
        if dist[i] < min_dist and not visited[i]:
            min_dist = dist[i]
            min_index = i
    return min_index


while False in visited:
    u = find_min_distance_vertex()
    if u == -1:  
        break
    
    for v in range(n):
        if weight[u][v] != 0 and not visited[v]:
            if dist[v] > dist[u] + weight[u][v]:
                dist[v] = dist[u] + weight[u][v]

    
    visited[u] = True

end_time = time.time()


print('Кратчайшее расстояние от' start, 'до' end, 'равно', dist[end])
print(f"Время выполнения: {end_time - start_time:.2f} секунд")
print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")