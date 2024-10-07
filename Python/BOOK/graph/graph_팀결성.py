import sys

n, m = map(int,sys.stdin.readline().split())
parent = [0] * (n+1)
<<<<<<< HEAD
for i in range(0,n+1):
=======

for i in range(1,n+1):
>>>>>>> 425949da4c9334f18dc9a3ed566a83e8d5ee8382
    parent[i] = i

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

for _ in range(m):
    op, a, b = map(int,sys.stdin.readline().split())
    if op == 0:
        union_parent(parent,a,b)
    else:
<<<<<<< HEAD
        print('YES') if find_parent(parent,a) == find_parent(parent,b) else print('NO')
=======
        print('YES') if parent[a] == parent[b] else print('NO')
>>>>>>> 425949da4c9334f18dc9a3ed566a83e8d5ee8382
