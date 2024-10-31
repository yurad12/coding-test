# https://www.acmicpc.net/problem/5427
import sys
input = sys.stdin.readline
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

case = int(input())
for _ in range(case):
    h, w = map(int, input().split())
    maze = [list(input().strip()) for _ in range(w)]

    fire_time = [[-1] * h for _ in range(w)]
    sang_time = [[-1] * h for _ in range(w)]
    sx, sy = -1, -1
    fires = deque()
    for i in range(w):
        for j in range(h):
            if maze[i][j] == '@':
                sang_time[i][j] = 0
                sx, sy = i, j
            if maze[i][j] == '*':
                fire_time[i][j] = 0
                fires.append((i,j))
            
    while fires:
        x, y = fires.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= w or ny < 0 or ny >= h:
                continue
            if maze[nx][ny] != '#' and fire_time[nx][ny] == -1:
                fires.append((nx,ny))
                fire_time[nx][ny] = fire_time[x][y] + 1
    
    sang = deque([(sx,sy,0)]) # start x, y, count
    answer = float('inf')
    escaped = False
    while sang:
        x, y, count = sang.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= w or ny < 0 or ny >= h:
                answer = min(answer, count + 1)
                escaped = True
                break
            if maze[nx][ny] == '#':
                continue
            if sang_time[nx][ny] == -1 and (fire_time[nx][ny] > count+1 or fire_time[nx][ny] == -1):
                sang_time[nx][ny] = count + 1
                sang.append((nx,ny,count+1))

    if not escaped:
        print("IMPOSSIBLE")
    else:
        print(answer)