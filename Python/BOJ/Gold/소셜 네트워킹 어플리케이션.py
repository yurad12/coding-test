# https://www.acmicpc.net/problem/7511
import sys
input = sys.stdin.readline

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

def solution(n, friends, relations):
    parent = [i for i in range(n)]
    for a, b in friends:
        union(parent, a, b)
    
    for u, v in relations:
        if find(parent, u) == find(parent, v):
            print(1)
        else:
            print(0)


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())

        k = int(input())
        friends = []
        for _ in range(k):
            friends.append(tuple(map(int, input().split())))
        
        m = int(input())
        relations = []
        for _ in range(m):
            relations.append(tuple(map(int, input().split())))

        print("Scenario %d:"%(i+1))
        solution(n, friends, relations)
        print()
