# https://www.acmicpc.net/problem/11779
import sys
input = sys.stdin.readline
from heapq import heappush, heappop

n = int(input())
m = int(input())
nodes = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, cost = map(int, input().split())
    nodes[a].append((b,cost))
start, end = map(int, input().split())

INF = int(1e9)
distance = [INF] * (n+1)
route = [[] for _ in range(n+1)]

q = []
heappush(q, (0, start))
distance[start] = 0
route[start] = [start]

while q:
    dist, now = heappop(q)
    if dist > distance[now]:
        continue

    for i in nodes[now]:
        cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            route[i[0]] = route[now] + [i[0]]
            heappush(q, (cost, i[0]))

print(distance[end])
print(len(route[end]))
print(route[end])