import sys
from collections import deque
#row:m, col:n
n, m = map(int, sys.stdin.readline().split())
matrix = [list(map(int,sys.stdin.readline().split())) for _ in range(m)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
tomato = []
for i in range(m):
    for j in range(n):
        if matrix[i][j] == 1:
            tomato.append((i,j))

def bfs(n,m):
    q = deque()
    for a, b in tomato:
        q.append((a,b))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx<0) | (nx>=m) | (ny<0) | (ny>=n):
                continue
            if matrix[nx][ny] == 0:
                matrix[nx][ny] = matrix[x][y] + 1
                q.append((nx,ny))
            elif matrix[nx][ny] == -1:
                continue
            elif matrix[nx][ny] >= 1:
                matrix[nx][ny] = min(matrix[nx][ny], matrix[x][y]+1)
    # print(matrix)
    day = 0
    for m in matrix:
        day = max(day,max(m))

    return day

day = bfs(n,m)
cnt = 0
for i in range(m):
    for j in range(n):
        if matrix[i][j] == 0:
            cnt += 1
if len(tomato) == n*m:
    print(0)
elif (len(tomato) == 0) | (cnt != 0):
    print(-1)
else:
    print(day-1)