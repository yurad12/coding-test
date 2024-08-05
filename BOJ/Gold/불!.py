# https://www.acmicpc.net/problem/4179

import sys
input = sys.stdin.readline
from collections import deque

R, C = map(int, input().split())
maze = []
sx, sy = -1, -1
fires = deque()
for i in range(R):
    data = list(input().strip())
    for j in range(C):
        if data[j] == "J":
            sx, sy = i, j
        if data[j] == "F":
            fires.append((i,j))
    maze.append(data)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

fire_time = [[-1] * C for _ in range(R)]
jihun_time = [[-1] * C for _ in range(R)]
q = deque([(sx,sy,0)])
jihun_time[sx][sy] = 0
answer = 0

# fire
for x, y in fires:
    fire_time[x][y] = 0

while fires:
    x, y = fires.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            continue
        if maze[nx][ny] == "." and fire_time[nx][ny] == -1:
            fire_time[nx][ny] = fire_time[x][y] + 1
            fires.append((nx,ny))

# jihun
while q:
    x, y, count = q.popleft()
    if x == 0 or x == R-1 or y == 0 or y == C-1:
        answer = count + 1
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            continue
        if maze[nx][ny] != ".":
            continue
        if (fire_time[nx][ny] == -1 or count+1 < fire_time[nx][ny]) and jihun_time[nx][ny] == -1:
            jihun_time[nx][ny] = count + 1
            q.append((nx,ny,count+1))

if answer:
    print(answer)
else:
    print("IMPOSSIBLE")
