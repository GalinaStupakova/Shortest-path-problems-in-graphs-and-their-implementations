n = int(input())
weight = [[int(x) for x in input().split()] for _ in range(n)]
inf = 1e8
for i in range(n):
    for j in range(n):
        if i != j and weight[i][j] == 0:  # Предполагаем, что 0 означает отсутствие ребра
            weight[i][j] = inf
dist = [0] * n 

for i in range(n):
    for u in range(n):
        for v in range(n):
            if weight[u][v] < inf and dist[u] + weight[u][v] < dist[v]:
                dist[v] = dist[u] + weight[u][v]
                if i == n - 1:
                    print("FALSE")
                    exit()

print("Нет отрицательных циклов")