import sys
from collections import deque
n, m, v = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
# 양방향 간선
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)
for i in range(n+1):
    graph[i] = sorted(graph[i])
# print(graph)
d_visited = [False]*(n+1)
b_visited = [False]*(n+1)

def dfs(graph, v, d_visited):
    d_visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not d_visited[i]:
            dfs(graph,i,d_visited)

def bfs(graph, v, b_visited):
    queue = deque([v])
    b_visited[v] = True
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for i in graph[node]:
            if not b_visited[i]:
                queue.append(i)
                b_visited[i] = True

dfs(graph,v,d_visited)
print()
bfs(graph,v,b_visited)