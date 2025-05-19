n = int(input())  
weight = [[int(x) for x in input().split()] for _ in range(n)]
inf = 1e8
for i in range(n):
    for j in range(n):
        if i != j and weight[i][j] == 0: 
           weight[i][j] = inf
for k in range(n):
    for i in range(n):
        for j in range(n):
            if (weight[i][k] != inf and weight[k][j] != inf and weight[i][j] > weight[i][k] + weight[k][j]):
                weight[i][j] = weight[i][k] + weight[k][j]
for k in range(n):
    for i in range(n):
        for j in range(n):
            if (weight[i][k] != inf and weight[k][j] != inf and weight[k][k] < 0):
                print(i+1 , j+1)
