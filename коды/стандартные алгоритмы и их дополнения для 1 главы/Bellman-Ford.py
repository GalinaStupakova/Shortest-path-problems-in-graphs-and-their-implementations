import time
import psutil

n = int(input())  # Чтение размера матрицы
weight = [[int(x) for x in input().split()] for _ in range(n)]
start = int(input()) - 1
inf = 1e8
for i in range(n):
    for j in range(n):
        if i != j and weight[i][j] == 0:  # Предполагаем, что 0 означает отсутствие ребра
            weight[i][j] = inf
dist= [inf]*n
dist[start] = 0
# Алгоритм Беллмана-Форда

for i in range(n - 1):
    for u in range(n):
        for v in range(n):
            if weight[u][v] < inf and dist[u] + weight[u][v] < dist[v]:
                dist[v] = dist[u] + weight[u][v]

# Проверка на наличие отрицательного цикла
for u in range(n):
    for v in range(n):
        if weight[u][v] < inf and dist[u] + weight[u][v] < dist[v]:
            print("FALSE")
            exit()

print(dist)
