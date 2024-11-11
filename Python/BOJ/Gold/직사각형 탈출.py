# https://www.acmicpc.net/problem/16973
import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
H, W, sr, sc, fr, fc = map(int, input().split())

prefix_sum = [[0] * (M+1) for _ in range(N+1)]
for i in range(N):
    for j in range(M):
        prefix_sum[i+1][j+1] = prefix_sum[i][j+1] + prefix_sum[i+1][j] - prefix_sum[i][j] + grid[i][j]

def place(x1, y1, x2, y2):
    return (prefix_sum[x2][y2] - prefix_sum[x1][y2] - prefix_sum[x2][y1] + prefix_sum[x1][y1]) == 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited = [[0] * (M) for _ in range(N)]

q = deque([(sr-1,sc-1)])

while q:
    x, y = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M or visited[nx][ny]:
            continue
        if nx+H > N or ny+W > M:
            continue
        if place(nx, ny, nx+H, ny+W):
            visited[nx][ny] = visited[x][y] + 1
            q.append((nx,ny))

answer = visited[fr-1][fc-1]
print(answer if answer else -1)
