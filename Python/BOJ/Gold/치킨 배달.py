# https://www.acmicpc.net/problem/15686

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
chickens, houses = [], []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            houses.append((i,j))
        elif graph[i][j] == 2:
            chickens.append((i,j))

visited = [False] * len(chickens)
answer = int(1e9)

def dfs(idx, cnt):
    global answer

    if cnt == m:
        total = 0
        for h in houses:
            dist = int(1e9)
            for c in range(len(chickens)):
                if visited[c]:
                    dist = min(dist, abs(h[0]-chickens[c][0])+abs(h[1]-chickens[c][1]))
            total += dist
        answer = min(answer, total)
        return
    
    for i in range(idx, len(chickens)):
        if not visited[i]:
            visited[i] = True
            dfs(i+1, cnt+1)
            visited[i] = False

dfs(0,0)
print(answer)