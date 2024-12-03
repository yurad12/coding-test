# https://www.acmicpc.net/problem/1916

from heapq import heappush, heappop
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
distance = [int(1e9)] * (n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, cost = map(int,input().split())
    graph[a].append((b,cost))
start, end = map(int,input().split())

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
    print(distance[end])

dijkstra(start)