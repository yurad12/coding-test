# https://www.acmicpc.net/problem/1261

from heapq import heappush, heappop

m, n = map(int,input().split())
maze = [list(map(int,input())) for _ in range(n)]
d = [[int(1e9)]*m for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

q = []
heappush(q,(0,0,0))
d[0][0] = 0

while q:
    dist, x, y = heappop(q)
    if d[x][y] < dist:
        continue
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or nx>=n or ny<0 or ny>=m:
            continue
        if maze[nx][ny] == 0:
            if d[nx][ny] > dist:
                d[nx][ny] = dist
                heappush(q,(d[nx][ny],nx,ny))
        else:
            if d[nx][ny] > dist+1:
                d[nx][ny] = dist + 1
                heappush(q,(d[nx][ny],nx,ny))
    
# print(d)
print(d[n-1][m-1])