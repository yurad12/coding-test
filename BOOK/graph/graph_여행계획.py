# https://www.acmicpc.net/problem/1976
import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
# n, m = map(int,sys.stdin.readline().split())

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


parent = [0] * (n+1)
for i in range(1,n+1):
    parent[i] = i

graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            union_parent(parent,i+1,j+1)

visit = list(map(int,sys.stdin.readline().split()))

result = True
for v in range(m-1):
    if find_parent(parent,visit[v]) != find_parent(parent,visit[v+1]):
        result = False
print('YES') if result else print('NO')
# print(parent)