import time
import psutil


filename = "graph_with_500vertex.txt" 
n = 1000  

# Инициализация матрицы весов
weight = [[0 if i == j else float('inf') for j in range(n)] for i in range(n)]

# Загрузка данных из файла
with open(filename) as f:
    for line in f:
        u, v, w = map(int, line.strip().split())
        weight[u][v] = w
        weight[v][u] = w  


# Алгоритм Флойда-Уоршелла
start_time = time.time()
for k in range(n):
    for i in range(n):
        for j in range(n):
            if weight[i][k] + weight[k][j] < weight[i][j]:
                weight[i][j] = weight[i][k] + weight[k][j]
end_time = time.time()

# Вывод результата
print('Расстояние между 500 и 700:' weight[500][700])
print(f"Время выполнения: {end_time - start_time:.2f} секунд")
print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")