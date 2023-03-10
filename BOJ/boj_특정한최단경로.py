# https://www.acmicpc.net/problem/1504

from heapq import heappush, heappop
import sys
input = sys.stdin.readline

n, e = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(e):
    a, b, cost = map(int,input().split())
    graph[a].append((b,cost))
    graph[b].append((a,cost))
v1, v2 = map(int,input().split())

def dijkstra(start,end):
    distance = [int(1e9)] * (n+1)
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
    return distance[end]

temp1 = dijkstra(1,v1) + dijkstra(v1,v2) + dijkstra(v2,n)
temp2 = dijkstra(1,v2) + dijkstra(v2,v1) + dijkstra(v1,n)
result = min(temp1,temp2)
if result >= int(1e9):
    result = -1
print(result)