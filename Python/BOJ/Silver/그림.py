# https://www.acmicpc.net/problem/1926
import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
picture = [list(map(int, input().split())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(i, j):
    q = deque([(i,j)])
    visited[i][j] = 1
    count = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if not visited[nx][ny] and picture[nx][ny]:
                q.append((nx,ny))
                visited[nx][ny] = 1
                count += 1
    
    return count

visited = [[0] * m for _ in range(n)]
answer = [0, 0]
for i in range(n):
    for j in range(m):
        if not visited[i][j] and picture[i][j]:
            count = bfs(i, j)
            if count:
                answer[0] += 1
                answer[1] = max(answer[1], count)
                
print(answer[0])
print(answer[1])