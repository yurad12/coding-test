# https://www.acmicpc.net/problem/1647

import sys

n, m = map(int,sys.stdin.readline().split())
parent = [0] * (n+1)
for i in range(1,n+1):
    parent[i] = i

result = 0
edges = []
for _ in range(m):
    a, b, cost = map(int,sys.stdin.readline().split())
    edges.append((cost,a,b))
edges.sort()

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for edge in edges:
    cost, a, b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost
        last = cost
print(result-last)