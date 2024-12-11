# https://www.acmicpc.net/problem/1922
# kruskal
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
edges = []
for _ in range(M):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
edges.sort()

def find(parent, x):
    if x != parent[x]:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = parent[a]
    b = parent[b]
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parent = [i for i in range(N+1)]
answer = 0

for cost, a, b in edges:
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        answer += cost

print(answer)
