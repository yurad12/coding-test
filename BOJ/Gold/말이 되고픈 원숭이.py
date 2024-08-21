# https://www.acmicpc.net/problem/1600

import sys
input = sys.stdin.readline
from collections import deque

K = int(input())
W, H = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(H)]

h = [(-2,-1), (-2,1), (-1,-2), (-1,2), (2,-1), (2,1), (1,-2), (1,2)]
d = [(-1,0), (1,0), (0,-1), (0,1)]

visited = [[[0] * (K+1) for _ in range(W)] for _ in range(H)] #[x][y][k]
q = deque([(0,0,0,0)]) # (x,y,count,k)
visited[0][0][0] = 1
answer = -1

while q:
    x, y, count, k = q.popleft()

    if x == H-1 and y == W-1:
        answer = count
        break

    for dx, dy in d:
        nx = x + dx
        ny = y + dy
        if nx < 0 or nx >= H or ny < 0 or ny >= W:
            continue
        if grid[nx][ny] or visited[nx][ny][k]:
            continue
        
        visited[nx][ny][k] = 1
        q.append((nx,ny,count+1,k))

    if k < K:
        for dx, dy in h:
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= H or ny < 0 or ny >= W:
                continue
            if grid[nx][ny] or visited[nx][ny][k+1]:
                continue
            
            visited[nx][ny][k+1] = 1
            q.append((nx,ny,count+1,k+1))
        
print(answer)