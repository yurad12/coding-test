import sys
input = sys.stdin.readline

g = int(input())
p = int(input())
gi = [int(input()) for _ in range(p)]
parent = [0]*(g+1)
for i in range(1,g+1):
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

result = 0
for i in range(p):
    temp = find_parent(parent,gi[i])
    if temp == 0:
        break
    union_parent(parent,temp,temp-1)
    result += 1

print(result)