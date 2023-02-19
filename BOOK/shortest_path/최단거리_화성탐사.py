import sys
from heapq import heappush, heappop

case = int(sys.stdin.readline())
dx = [-1,1,0,0]
dy = [0,0,-1,1]
inf = int(1e9)

while case != 0:
    n = int(sys.stdin.readline())
    graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
    distance = [[inf] * n for _ in range(n)]
    x, y = 0, 0
    q = [(graph[x][y], x, y)]
    distance[x][y] = graph[x][y]

    while q:
        dist, x, y = heappop(q)
        if distance[x][y] < dist:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx<0) | (nx>=n) |(ny<0) | (ny>=n):
                continue
            cost = dist + graph[nx][ny]
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heappush(q,(cost,nx,ny))
    case -= 1
    print(distance[n-1][n-1])