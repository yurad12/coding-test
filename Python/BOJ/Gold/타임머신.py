# https://www.acmicpc.net/problem/11657

import sys
input = sys.stdin.readline

v, e = map(int, input().split())
INF = int(1e9)
edges = []
dist = [INF] * (v+1)
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((a,b,cost))

def bf(start):
    dist[start] = 0
    for i in range(v):
        for j in range(e):
            a, b, cost = edges[j]
            if dist[a] != INF and dist[b] > dist[a] + cost:
                dist[b] = dist[a] + cost
                if i == v-1:
                    return False
    return True
if not bf(1):
    print(-1)
else:
    for i in dist[2:]:
        if i != INF:
            print(i)
        else:
            print(-1)