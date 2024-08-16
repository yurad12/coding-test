# https://www.acmicpc.net/problem/2583

import sys
input = sys.stdin.readline

m, n, k = map(int, input().split())
graph = [[0]*n for _ in range(m)]
for _ in range(k):
    lx, ly, rx, ry = map(int, input().split())
    for i in range(ly,ry):
        for j in range(lx,rx):
            graph[i][j] = 1

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
    stack = [(x,y)]
    count = 0
    visited[x][y] = True

    while stack:
        cx, cy = stack.pop()
        count += 1
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if not visited[nx][ny] and not graph[nx][ny]:
                visited[nx][ny] = True
                stack.append((nx,ny))

    return count

answer = []
visited = [[False] * n for _ in range(m)]
for i in range(m):
    for j in range(n):
        if not graph[i][j] and not visited[i][j]:
            count = dfs(i,j)
            answer.append(count)
answer.sort()
print(len(answer))
print(*answer)
