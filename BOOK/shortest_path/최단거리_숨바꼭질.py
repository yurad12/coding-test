import sys
from heapq import heappush, heappop

n, m = map(int,sys.stdin.readline().split())
inf = int(1e9)
distance = [inf] * (n+1)
graph = [[]*(n+1) for _ in range(n+1)]
for _ in range(m):
    x, y = map(int,sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)
print(graph)
q = []
heappush(q,(0,1))
distance[0] = 0
distance[1] = 0
while q:
    dist, now = heappop(q)
    if distance[now] < dist:
        continue
    for i in graph[now]:
        cost = dist + 1
        if cost < distance[i]:
            distance[i] = cost
            heappush(q,(cost,i))
    print(distance)
num = n+1
m_dist = 0
cnt = 0
for i in range(1,n+1):
    if distance[i] == inf:
        continue
    if distance[i] == max(distance):
        cnt += 1
        num = min(num,i)
        m_dist = distance[i]

print(num, m_dist, cnt)