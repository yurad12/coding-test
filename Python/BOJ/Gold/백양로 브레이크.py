# https://www.acmicpc.net/problem/11562
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(m): # 단1, 양0
    u, v, b = map(int, input().split())
    graph[u][v] = 0
    if b:
        graph[v][u] = 0
    else:
        graph[v][u] = 1 # 단 -> 양 변경 비용

for i in range(1, n+1):
    graph[i][i] = 0

for k in range(n+1):
    for a in range(n+1):
        for b in range(n+1):
            if graph[a][b] > graph[a][k] + graph[k][b]: # min() 안쓰면 python3으로 통과 가능
                graph[a][b] = graph[a][k] + graph[k][b]

k = int(input())
questions = [list(map(int, input().split())) for _ in range(k)]
for a, b in questions:
    print(graph[a][b])
