# https://www.acmicpc.net/problem/14940

import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
result = [[-1]*m for _ in range(n)]

tx, ty = 0, 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            result[i][j] = 0
            tx, ty = i, j
        elif graph[i][j] == 0:
            result[i][j] = 0

q = deque([(tx,ty)])
while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if not result[nx][ny] or result[nx][ny] != -1:
            continue
        result[nx][ny] = result[x][y]+1
        q.append((nx,ny))

for i in range(n):
    for j in range(m):
        print(result[i][j], end = ' ')
    print()