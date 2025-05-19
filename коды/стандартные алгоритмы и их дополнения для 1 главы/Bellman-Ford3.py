n = int(input())
weight = [list(map(int, input().split())) for _ in range(n)]
start = int(input()) - 1
inf = 10**8

for i in range(n):
    for j in range(n):
        if i != j and weight[i][j] == 0:
            weight[i][j] = inf

dist = [inf] * n
dist[start] = 0
parent = [-1] * n

# Алгоритм Беллмана-Форда (n - 1 итерация)
for _ in range(n - 1):
    for u in range(n):
        for v in range(n):
            if dist[u] + weight[u][v] < dist[v]:
                dist[v] = dist[u] + weight[u][v]
                parent[v] = u
# Проверка на наличие отрицательного цикла
owned = [False] * n
for u in range(n):
    for v in range(n):
        if dist[u] + weight[u][v] < dist[v]:
            print("FALSE")

            # Шаг 1: найти вершину в цикле
            x = v
            for _ in range(n):
                x = parent[x]
            # Шаг 2: пометить сам цикл
            owned[x] = True
            # Шаг 3: распространить "заразу" по всем достижимым из цикла вершинам
            for _ in range(n):
                for a in range(n):
                    if owned[a]:
                        for b in range(n):
                            if weight[a][b] < inf:
                                owned[b] = True


unreachable = [i + 1 for i in range(len(owned)) if owned[i]]
if unreachable:
    unreachable.sort()
    print("Нет кратчайшего пути до вершин:", *unreachable)
else:
    unreachable = [i + 1 for i in range(n) if dist[i] >= inf]
    if unreachable:
        print("Нет кратчайшего пути до вершин:", *unreachable)
    else:
        print("Кратчайший путь существует до всех вершин.")
print(dist)
