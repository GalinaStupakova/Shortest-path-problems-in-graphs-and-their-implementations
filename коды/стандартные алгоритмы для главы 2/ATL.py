n = int(input())
weight = [[int(x) for x in input().split()] for _ in range(n)]
start = int(input()) - 1
end = int(input()) - 1
landmark = int(input()) - 1
inf = 1e8
heruistic=[]


dist_l = [inf] * n
dist_l[landmark] = 0
visited_l = [False] * n

def gofrom():
 index = 0
 distmin = inf
 for i in range(n):
  if dist_l[i] < distmin and visited_l[i]== False:
   distmin = dist_l[i]
   index = i
 return index

dist_f = [inf] * n
dist_f[start] = 0
visited_g = [False] * n

def gofrom2():
 index2 = -1
 distmin2 = inf
 for i in range(n):
  if not visited_g[i] and dist_f[i] < inf:
    f = dist_f[i] + heruistic[i]  # g + h
    if f < distmin2:
      distmin2 = f
      index2 = i
 return index2

while False in visited_l:
 u = gofrom()
 for v in range(n):
  if weight[u][v] !=0 and (not visited_l[v]): #идем по соседям текущей вершины 
   dist_l[v] = min(dist_l[v], dist_l[u]+weight[u][v])
 visited_l[u]=True

for i in range(len(dist_l)):
  h = max(dist_l[end] - dist_l[i], dist_l[i] - dist_l[end])
  heruistic.append(h)

while False in visited_g:
    u = gofrom2()
    if u == -1:
      #reak
    if u == end:
        break
    visited_g[u] = True
    for v in range(n):
        if weight[u][v] != 0 and not visited_g[v]:
            middle = dist_f[u] + weight[u][v]
            if middle < dist_f[v]:
                dist_f[v] = middle




print("Кратчайшее расстояние от", start + 1, "до", end + 1, "через", landmark + 1, ":", dist_f[end])