n = int(input())
weight = [[int(x) for x in input().split()] for i in range(n)]
start = int(input()) - 1
inf = 1e8
visited = [False]*n # список из n элементов false, когда будем проверять станет True
dist = [inf]*n
dist[start] = 0 # элемент под индексом старт равен 0

def gofrom():
	index = 0
	distmin = inf
	for i in range(n):
		if dist[i] < distmin and visited[i]== False:
			distmin = dist[i]
			index = i
	return index

while False in visited:
	u = gofrom()
	for v in range(n):
		if weight[u][v] !=0 and (not visited[v]): #идем по соседям текущей вершины 
			dist[v] = min(dist[v], dist[u]+weight[u][v])
	visited[u]=True
for i in range(len(dist)):
	print('Расстояние от', start + 1, "до", i +1, 'равно', dist[i])
