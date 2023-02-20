# https://www.acmicpc.net/problem/4485

import sys
from heapq import heappush, heappop

# case = int(sys.stdin.readline())
inf = int(1e9)
dx = [-1,1,0,0]
dy = [0,0,-1,1]
cnt = 0

while True:
# while case != 0:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    graph = []
    for i in range(n):
        graph.append(list(map(int,sys.stdin.readline().split())))
    distance = [[inf] * n for _ in range(n)]
    q = [(graph[0][0],0,0)]
    distance[0][0] = graph[0][0]

    while q:
        dist, x, y = heappop(q)
        if distance[x][y] < dist:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx<0) | (nx>=n) | (ny<0) | (ny>=n):
                continue
            cost = dist + graph[nx][ny]
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heappush(q,(cost,nx,ny))
    # print(distance[n-1][n-1])
    cnt += 1
    print('Problem %d: %d' %(cnt, distance[n-1][n-1]))
    # case -= 1