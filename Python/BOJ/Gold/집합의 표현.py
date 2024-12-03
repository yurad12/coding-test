# https://www.acmicpc.net/problem/1717
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())

def find(parent, x):
    if x != parent[x]:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


parent = [i for i in range(n+1)]
answer = []
for _ in range(m):
    op, a, b = map(int, input().split())
    if op == 0:
        union(parent, a, b)
        continue
    
    if find(parent, a) == find(parent, b):
        answer.append('YES')
    else:
        answer.append('NO')

for ans in answer:
    print(ans)