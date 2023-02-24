# https://www.acmicpc.net/problem/2178

from collections import deque

n, m = map(int,input().split())
array = [list(map(int,input())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

q = deque()
q.append((0,0))

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (nx<0) | (nx>=n) | (ny<0) | (ny>=m):
            continue
        dist = array[x][y] + 1
        if array[nx][ny] > dist:
            array[nx][ny] = dist
            q.append((nx,ny))
            continue
        if array[nx][ny] == 1:
            array[nx][ny] = array[x][y] + 1
            q.append((nx,ny))

print(array[n-1][m-1])