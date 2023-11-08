# https://www.acmicpc.net/problem/16236
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
array = [list(map(int,input().split())) for _ in range(n)]

cx, cy = 0, 0
for i in range(n):
    for j in range(n):
        if array[i][j] == 9:
            cx, cy = i, j
            array[cx][cy] = 0
size = 2

dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 거리구하기
def bfs():
    q = deque()
    q.append((cx,cy))
    dist = [[-1]*n for _ in range(n)]
    dist[cx][cy] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if dist[nx][ny] == -1 and array[nx][ny] <= size:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx,ny))
    return dist

# 물고기 찾기
def find(dist):
    x, y = 0, 0
    min_dist = int(1e9)
    for i in range(n):
        for j in range(n):
            if dist[i][j] != -1 and 1 <= array[i][j] and array[i][j] < size:
                if dist[i][j] < min_dist:
                    x, y = i, j
                    min_dist = dist[i][j]
    if min_dist == int(1e9):
        return None
    else:
        return x,y,min_dist

# 탐색
result = 0
count = 0

while True:
    loc = find(bfs())
    if loc == None:
        print(result)
        break
    else:
        cx, cy = loc[0], loc[1]
        result += loc[2]
        array[cx][cy] = 0
        count += 1
        if count >= size:
            size += 1
            count = 0
