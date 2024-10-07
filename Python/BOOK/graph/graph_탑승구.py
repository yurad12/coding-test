# https://www.acmicpc.net/problem/10775
import sys

g = int(sys.stdin.readline()) # 탑승구 수
p = int(sys.stdin.readline()) # 비행기 수
parent = [0] * (g+1)
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

gi = list(int(sys.stdin.readline()) for _ in range(p))
result = 0
for i in range(p):
    temp = find_parent(parent,gi[i])
    if temp == 0:
        break
    union_parent(parent,temp,temp-1)
    result += 1
    # print(parent)
print(result)