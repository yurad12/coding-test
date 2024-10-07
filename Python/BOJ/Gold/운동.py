# https://www.acmicpc.net/problem/1956

## 플로이드 워셜 -> pypy3
import sys
input = sys.stdin.readline
INF = float('inf')

v, e = map(int, input().split())
graph = [[INF] * (v+1) for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, v+1):
    for a in range(1, v+1):
        for b in range(1, v+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
        
answer = INF
for i in range(1, v+1):
    answer = min(answer, graph[i][i])

if answer == INF:
    print(-1)
else:
    print(answer)

## 다익스트라 ->  메모리 초과
from heapq import heappush, heappop
INF = float('inf')

v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]
distance = [[INF] * (v+1) for _ in range(v+1)]
q = []
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    heappush(q, (c,a,b))

while q:
    dist, a, b = heappop(q)
    if a == b:
        print(dist)
        break

    if distance[a][b] < dist:
        continue

    for i in graph[b]:
        if dist + i[1] < distance[a][i[0]]:
            distance[a][i[0]] = dist + i[1]
            heappush(q, (distance[a][i[0]],a,i[0]))
else:
    print(-1)
