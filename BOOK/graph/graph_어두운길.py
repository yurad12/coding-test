# https://www.acmicpc.net/problem/6497
import sys

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

while True:
    n, m = map(int,sys.stdin.readline().split())
    if n == 0 and m == 0:
        break
    parent = [0] * n
    for i in range(n):
        parent[i] = i

    graph = []
    for _ in range(m):
        a, b, cost = map(int,sys.stdin.readline().split())
        graph.append((cost,a,b))
    graph.sort()

    max_sum = 0
    min_sum = 0
    for g in graph:
        cost, a, b = g
        max_sum += cost
        if find_parent(parent,a) != find_parent(parent,b):
            union_parent(parent,a,b)
            min_sum += cost
    print(max_sum-min_sum)