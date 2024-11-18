# https://www.acmicpc.net/problem/7569
import sys
input = sys.stdin.readline
from collections import deque

M, N, H = map(int, input().split())
boxes = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

INF = int(1e9)
dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

tomatoes = [[[INF] * M for _ in range(N)] for _ in range(H)]
q = deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if boxes[i][j][k] == 1:
                q.append((i,j,k))
                tomatoes[i][j][k] = 0

while q:
    x, y, z = q.popleft()

    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if nx < 0 or nx >= H or ny < 0 or ny >= N or nz < 0 or nz >= M:
            continue
        if boxes[nx][ny][nz] == 0 and tomatoes[nx][ny][nz] == INF:
            tomatoes[nx][ny][nz] = tomatoes[x][y][z] + 1
            q.append((nx,ny,nz))

def get_answer():
    answer = 0
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if boxes[i][j][k] != -1:
                    if tomatoes[i][j][k] != INF:
                        answer = max(answer, tomatoes[i][j][k])
                    else:
                        answer = -1
                        return answer
    return answer

print(get_answer())