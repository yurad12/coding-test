# https://www.acmicpc.net/problem/2606

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)

def bfs(graph, start, visited):
    result = 0
    q = deque([start])
    visited[start] = True

    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                result += 1
    return result

print(bfs(graph,1,visited))
