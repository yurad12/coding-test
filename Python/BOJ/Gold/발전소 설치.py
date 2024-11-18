# https://www.acmicpc.net/problem/1277
import sys
input = sys.stdin.readline
import math
from heapq import heappush, heappop

N, W = map(int, input().split())
M = float(input())
stations = [list(map(int, input().split())) for _ in range(N)]

graph = [[] for _ in range(N+1)]
for _ in range(W):
    a, b = map(int, input().split())
    graph[a].append((b, 0))
    graph[b].append((a, 0))

for i in range(N):
    for j in range(i+1, N):
        x1, y1 = stations[i]
        x2, y2 = stations[j]
        
        dist = math.sqrt(abs(x1-x2) ** 2 + abs(y1-y2) ** 2)
        if dist <= M:
            graph[i+1].append((j+1, dist))
            graph[j+1].append((i+1, dist))

INF = int(1e9)
distance = [INF] * (N+1)
q = []

distance[1] = 0
heappush(q, (0, 1))

while q:
    dist, now = heappop(q)

    if distance[now] < dist:
        continue

    for next in graph[now]:
        cost = next[1] + dist
        if cost < distance[next[0]]:
            distance[next[0]] = cost
            heappush(q, (cost, next[0]))

print(int(distance[N] * 1000))