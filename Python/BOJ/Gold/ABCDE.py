# https://www.acmicpc.net/problem/13023
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x, depth):
    print(x)
    if depth == 5:
        print(1)
        sys.exit(0)
    
    visited[x] = 1
    for nx in graph[x]:
        if not visited[nx]:
            dfs(nx, depth+1)
    visited[x] = 0

visited = [0] * N
for i in range(N):
    print("start")
    dfs(i, 1)

print(0)