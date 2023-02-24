# https://www.acmicpc.net/problem/1753

import sys
from heapq import heappush, heappop
input = sys.stdin.readline

v, e = map(int,input().split())
start = int(input())
graph = [[] for _ in range(v+1)]
inf = int(1e9)
distance = [inf] * (v+1)
for _ in range(e):
    a, b, c = map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heappush(q,(cost,i[0]))

dijkstra(start)

for i in range(1,v+1):
    if distance[i] == inf:
        print('INF')
    else:
        print(distance[i])