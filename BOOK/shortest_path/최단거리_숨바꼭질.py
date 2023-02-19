import sys
from heapq import heappush, heappop

n, m = map(int,sys.stdin.readline().split())
inf = int(1e9)
graph = [[] for _ in range(n+1)]
distance = [inf] * (n+1)
for _ in range(m):
    a, b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def dijkstra(start):
    q = []
    heappush(q,(0,start))
    distance[0] = 0
    distance[start] = 0
    while q:
        dist, now = heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = distance[now] + 1
            if cost < distance[i]:
                distance[i] = cost
                heappush(q,(cost,i))
    # print(distance)

dijkstra(1)

num = n+1
m_dist = max(distance)
count = 0
for i in range(1, n+1):
    if distance[i] == max(distance):
        num = min(num,i)
        count += 1
print(num,m_dist,count)