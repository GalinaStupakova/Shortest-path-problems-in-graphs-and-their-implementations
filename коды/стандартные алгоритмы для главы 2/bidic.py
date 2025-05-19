n = int(input())
weight = [[int(x) for x in input().split()] for _ in range(n)]
start = int(input()) - 1
end = int(input()) - 1
inf = 1e8

dist_start = [inf] * n
dist_end = [inf] * n
dist_start[start] = 0
dist_end[end] = 0

visited_start = [False] * n
visited_end = [False] * n

# Функция выбора ближайшей вершины
def get_min_index(dist, visited):
    index = -1
    min_dist = inf
    for i in range(n):
        if dist[i] < min_dist and not visited[i]:
            min_dist = dist[i]
            index = i
    return index
flag = False
while flag==False:
    # Находим минимальную вершину для прямого поиска
    u = get_min_index(dist_start, visited_start)
    # Находим минимальную вершину для обратного поиска
    v = get_min_index(dist_end, visited_end)

    # Если обе вершины недоступны, выходим
    if u == -1 and v == -1:
        break

    # Прямой шаг от старта
    if u != -1:
        visited_start[u] = True
        for neighbor in range(n):
            if weight[u][neighbor] > 0 and not visited_start[neighbor]:
                dist_start[neighbor] = min(dist_start[neighbor], dist_start[u] + weight[u][neighbor])

    # Обратный шаг от конца
    if v != -1:
        visited_end[v] = True
        for neighbor in range(n):
            if weight[neighbor][v] > 0 and not visited_end[neighbor]:
                dist_end[neighbor] = min(dist_end[neighbor], dist_end[v] + weight[neighbor][v])

    # Проверяем, встретились ли две стороны (если вершина посещена с обеих сторон)
    for i in range(n):
        if visited_start[i] and visited_end[i]:
            total = dist_start[i] + dist_end[i]
            flag = True
            break

# Перебираем все пары вершин, чтобы найти минимальное расстояние
shortest = inf
for u in range(n):
    if visited_start[u]:
        for v in range(n):
            if visited_end[v] and weight[u][v] > 0:
                total = dist_start[u] + weight[u][v] + dist_end[v]
                if total < shortest:
                    shortest = total

# Если путь найден, выводим результат

print('Расстояние от', start + 1, "до", end +1, 'равно', shortest)