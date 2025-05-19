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
        weight[v][u] = w  # для неориентированного графа

# Инициализация расстояний
dist = [inf] * n
dist[start] = 0

# Алгоритм Беллмана-Форда
start_time = time.time()

for i in range(n - 1):
    for u in range(n):
        for v in range(n):
            if weight[u][v] < inf and dist[u] + weight[u][v] < dist[v]:
                dist[v] = dist[u] + weight[u][v]

# Проверка на отрицательные циклы
has_negative_cycle = False
for u in range(n):
    for v in range(n):
        if weight[u][v] < inf and dist[u] + weight[u][v] < dist[v]:
            has_negative_cycle = True
            break
    if has_negative_cycle:
        break

end_time = time.time()

# Вывод результатов
if has_negative_cycle:
    print("FALSE (обнаружен отрицательный цикл)")
else:
    print('Расстояние от', start + 1, "до", end + 1, 'равно', dist[end])

print(f"Время выполнения: {end_time - start_time:.2f} секунд")
print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")