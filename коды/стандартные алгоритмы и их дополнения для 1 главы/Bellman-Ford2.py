n = int(input())  # Чтение размера матрицы
weight = [[int(x) for x in input().split()] for _ in range(n)]
start = int(input()) - 1
inf = 1e8
for i in range(n):
    for j in range(n):
        if i != j and weight[i][j] == 0:
            weight[i][j] = inf

dist = [inf] * n
dist[start] = 0
parent = [-1] * n 
for i in range(n - 1):
    for u in range(n):
        for v in range(n):
            if weight[u][v] < inf and dist[u] + weight[u][v] < dist[v]:
                dist[v] = dist[u] + weight[u][v]
                parent[v] = u

for u in range(n):
    for v in range(n):
        if weight[u][v] < inf and dist[u] + weight[u][v] < dist[v]:
            print("FALSE")
            
            cycle_start = v
            for _ in range(n):  # Проходим ещё n раз, чтобы попасть в цикл
                cycle_start = parent[cycle_start]

            # Восстанавливаем сам цикл
            cycle = []
            current = cycle_start
            while True:
                cycle.append(current)
                current = parent[current]
                if current == cycle_start:
                    break
            cycle.append(cycle_start)

            cycle.reverse()  # Печатаем от начала до конца
            cycle = [i + 1 for i in cycle]
            print("Отрицательный цикл:", " -> ".join(map(str, cycle)))
            exit()

# Если отрицательного цикла нет, выводим расстояния
print(dist)
