# https://www.acmicpc.net/problem/2206

import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]

visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

q = deque([(0,0,0)])
visited[0][0][0] = 1
answer = -1

while q:
    x, y, wall = q.popleft()
    if x == N-1 and y == M-1:
        answer = visited[x][y][wall]
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        
        # 벽 안 부수는 경우
        if not graph[nx][ny] and not visited[nx][ny][wall]:
            visited[nx][ny][wall] = visited[x][y][wall] + 1
            q.append((nx,ny,wall))
        # 벽 부수는 경우
        if graph[nx][ny] and not wall and not visited[nx][ny][wall]:
            visited[nx][ny][1] = visited[x][y][wall] + 1
            q.append((nx,ny,1))

print(answer)