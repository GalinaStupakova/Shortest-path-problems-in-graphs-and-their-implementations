n = int(input())
weight = [[int(x) for x in input().split()] for _ in range(n)]

inf = 1e8
# Массив предков для восстановления пути
parent = [[-1 for _ in range(n)] for _ in range(n)]

# Инициализация весов и массива parent
for i in range(n):
    for j in range(n):
        if i != j and weight[i][j] == 0:
            weight[i][j] = inf
        elif i != j:
            parent[i][j] = i  # Указываем, что текущая вершина пришла из вершины i

for k in range(n):
    for i in range(n):
        for j in range(n):
            if (weight[i][k] != inf and weight[k][j] != inf and weight[i][j] > weight[i][k] + weight[k][j]):
                weight[i][j] = weight[i][k] + weight[k][j]
                parent[i][j] = parent[k][j] 

# Проверка на отрицательные циклы
for i in range(n):
    if weight[i][i] < 0:

        # Восстановление отрицательного цикла
        cycle = []
        visited = [False] * n
        node = i

        # Переходим по предшествующим вершинам, пока не найдем повторяющуюся вершину
        while not visited[node]:
            visited[node] = True
            cycle.append(node)
            node = parent[i][node]  # Переходим к предшествующей вершине

        cycle.append(i)
        cycle.reverse()
        cycle = [i + 1 for i in cycle]
        print("Цикл:", " -> ".join(map(str, cycle)))
        exit()
print(weight)