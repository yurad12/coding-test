# https://www.acmicpc.net/problem/17835
import sys
input = sys.stdin.readline
from heapq import heappush, heappop

N, M, K = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[b].append((a,c))
starts = list(map(int, input().split()))

INF = float('inf')
distance = [INF] * (N+1)
q = []

for i in starts:
    distance[i] = 0
    heappush(q, (0,i))

while q:
    dist, now = heappop(q)

    if distance[now] < dist:
        continue

    for i in graph[now]:
        cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heappush(q, (cost,i[0]))

max_value = -1
for i in range(1,N+1):
    if distance[i] < INF and distance[i] > max_value:
        max_value = distance[i]

for i in range(1, N+1):
    if distance[i] == max_value:
        print(i)
        break
print(max_value)