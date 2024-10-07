# https://www.acmicpc.net/problem/10026
import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
picture = [list(input().strip()) for _ in range(N)]

blind_picture = [[''] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if picture[i][j] == 'B':
            blind_picture[i][j] = 'B'
        else:
            blind_picture[i][j] = 'G'

def bfs(x, y, picture, visited):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    q = deque([(x,y)])
    visited[x][y] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N or visited[nx][ny]:
                continue

            if picture[x][y] == picture[nx][ny]:
                q.append((nx,ny))
                visited[nx][ny] = 1

visited_normal = [[0] * N for _ in range(N)]
visited_colorblind = [[0] * N for _ in range(N)]
answer = [0,0]

for i in range(N):
    for j in range(N):
        if not visited_normal[i][j]:
            bfs(i,j,picture,visited_normal)
            answer[0] += 1
        if not visited_colorblind[i][j]:
            bfs(i,j,blind_picture,visited_colorblind)
            answer[1] += 1
    
print(*answer)
