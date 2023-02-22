import sys
from heapq import heappush, heappop

n, m, c  = map(int,sys.stdin.readline().split())
inf = int(1e9)
distance = [inf] * (n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y, z = map(int,sys.stdin.readline().split())
    graph[x].append((y,z))

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
dijkstra(c)

ci = 0; ti = 0
for d in range(1,n+1):
    if 0 < distance[d] < inf:
        ci += 1
        ti = max(ti,distance[d])
print(distance)
print(ci,ti)