# https://www.acmicpc.net/problem/2617
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
beads = [tuple(map(int, input().split())) for _ in range(M)]

light = [[] for _ in range(N+1)]
heavy = [[] for _ in range(N+1)]
for a, b in beads:
    light[b].append(a)
    heavy[a].append(b)

def dfs(start, graph):
    stack = [start]
    visited = set()

    while stack:
        now = stack.pop()
        for i in graph[now]:
            if i not in visited:
                visited.add(i)
                stack.append(i)
    
    return visited

for i in range(1, N+1):
    light[i] = list(dfs(i, light))
    heavy[i] = list(dfs(i, heavy))

answer = 0
mid = (N+1) // 2
for i in range(1, N+1):
    if mid <= len(light[i]) or mid <= len(heavy[i]):
        answer += 1

print(answer)