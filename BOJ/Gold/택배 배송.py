# https://www.acmicpc.net/problem/5972
# 최단경로 -> 다익스트라

import sys
input = sys.stdin.readline
from heapq import heappush, heappop

n, m = map(int, input().split())
farm = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    farm[a].append((b,c))
    farm[b].append((a,c))

INF = int(1e9)
distance = [INF] * (n+1)

def dijkstra(start):
    q = []
    heappush(q, (0,start))
    distance[start] = 0

    while q:
        dist, now = heappop(q)
        for i in farm[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heappush(q, (cost,i[0]))

dijkstra(1)
print(distance[n])
