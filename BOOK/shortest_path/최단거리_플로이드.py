# https://www.acmicpc.net/problem/11404

import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
inf = int(1e9)
graph = [[inf]*(n+1) for _ in range(n+1)]
for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b] = 0
for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    if c < graph[a][b]:
        graph[a][b] = c
    # graph[a][b] = min(graph[a][b],c)
    # 시간 조금 더 걸림

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])

for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] == inf:
            print(0,end =' ')
        else:
            print(graph[i][j], end=' ')
    print()