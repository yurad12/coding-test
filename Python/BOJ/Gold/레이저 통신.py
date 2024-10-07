'''
https://www.acmicpc.net/problem/6087
(1,1), (0,1) (0,2)...(0,5), (1,5)...(6,5), (6,6)
bfs로 c1->c2 가는 길을 찾으면서, 방향이 몇 번 꺾이는지 기록
1. 큐: x,y,거울 개수, 방향
2. visited 배열: x, y, 방향 -> 해당 방향에서 온 좌표 x,y
3. bfs
 1) 방향이 같으면, 거울 추가x
 2) 방향이 다르면, 거울 추가
'''

import sys
input = sys.stdin.readline
from collections import deque
INF = int(1e9)

W, H = map(int, input().split())
graph = [list(input().strip()) for _ in range(H)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
c = []
for i in range(H):
    for j in range(W):
        if graph[i][j] == 'C':
            c.append((i,j))

visited = [[[INF] * 4 for _ in range(W)] for _ in range(H)]
x, y = c[0][0], c[0][1]

q = deque([(x,y,0,-1)])
answer = INF

while q:
    x, y, mirror, direc = q.popleft()
    
    if (x,y) == c[1]:
        answer = min(answer, mirror)
        continue

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= H or ny < 0 or ny >= W or graph[nx][ny] == '*':
            continue

        if direc == i or direc == -1:
            if visited[nx][ny][i] > mirror:
                visited[nx][ny][i] = mirror
                q.append((nx,ny,mirror,i))
        else:
            if visited[nx][ny][i] > mirror+1:
                visited[nx][ny][i] = mirror + 1
                q.append((nx,ny,mirror+1,i))

print(answer)