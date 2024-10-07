import sys

n, m = map(int,sys.stdin.readline().split())
inf = int(1e9)
graph = [[inf]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            graph[i][j] = 0
for _ in range(m):
    v1, v2 = map(int,sys.stdin.readline().split())
    graph[v1][v2] = 1
    graph[v2][v1] = 1
x, k = map(int,sys.stdin.readline().split())

# 1 -> k -> x
for l in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][l]+graph[l][b])

if graph[1][k]+graph[k][x] >= inf:
    print(-1)
else:
    print(graph[1][k]+graph[k][x])