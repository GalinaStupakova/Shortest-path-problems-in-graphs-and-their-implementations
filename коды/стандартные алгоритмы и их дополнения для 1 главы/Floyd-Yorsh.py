import time
import psutil
n = int(input())
weight = [[int(x) for x in input().split()] for _ in range(n)]
inf = 1e8
for i in range(n):
    for j in range(n):
        if i != j and weight[i][j] == 0:  # Предполагаем, что 0 означает отсутствие ребра
            weight[i][j] = inf

for k in range(n):
	for i in range(n):
		for j in range(n):
			if (weight[i][k] != inf and weight[k][j] != inf and weight[i][j] > weight[i][k] + weight[k][j]):
				weight[i][j] = weight[i][k] + weight[k][j]
end_time = time.time()
for l in weight: 
    for i2 in l: 
        print(i2, end=' ') 
    print()
