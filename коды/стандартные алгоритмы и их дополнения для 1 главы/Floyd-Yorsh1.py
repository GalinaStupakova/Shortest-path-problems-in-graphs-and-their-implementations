n = int(input())
weight = [[int(x) for x in input().split()] for _ in range(n)]
inf = 1e8
for k in range(n):
	for i in range(n):
		for j in range(n):
			if (weight[i][k] != inf and weight[k][j] != inf and weight[i][j] > weight[i][k] + weight[k][j]):
				weight[i][j] = weight[i][k] + weight[k][j]
for i in range(n):
	if d[i][i]<0:
		flag = False
	else:
		flag = True
if flag == False:
	print("В графе есть отрицательный цикл")
else:
	print(d)
