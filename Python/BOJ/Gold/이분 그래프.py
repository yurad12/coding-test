# https://www.acmicpc.net/problem/1707
import sys
input = sys.stdin.readline
from collections import deque

def split(start):
    q = deque([start])
    colors[start] = 1

    while q:
        now = q.popleft()
        for i in graph[now]:
            if colors[i] == 0:
                colors[i] = -colors[now]
                q.append(i)
            elif colors[i] == colors[now]:
                return False
    
    return True

k = int(input())
for _ in range(k):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    colors = [0] * (v+1)
    bipartite = True
    for i in range(1, v+1):
        if colors[i]:
            continue
        if not split(i):
            bipartite = False
            break
    
    if bipartite:
        print("YES")
    else:
        print("NO")