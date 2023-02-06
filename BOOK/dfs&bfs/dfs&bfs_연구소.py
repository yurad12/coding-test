import sys
from collections import deque
from itertools import combinations
import copy
n, m = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
# print(graph)
virus = []
for i in range(n):
    for j in range(m):
        if graph[i][j]==2:
            virus.append((i,j))
random = list(combinations(range(n*m),3))
dx = [-1,1,0,0]
dy = [0,0,-1,1]
safety = 0

# 상하좌우 살펴서 2 퍼뜨리기
def bfs(x,y):
    queue = deque()
    for i,j in virus:
        queue.append((i,j))
    while queue:
        x, y  = queue.popleft()
        # print('x : %d, y : %d' % (x, y))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx<0) | (nx>=n) | (ny<0) | (ny>=m):
                continue
            if (copy_graph[nx][ny] == 0):
                copy_graph[nx][ny] = 2
                queue.append((nx,ny))
            elif copy_graph[nx][ny] == 1:
                continue
    c=0
    for i in copy_graph:
        c += i.count(0)
    # print("finish %d" %(c))
    return c
    
for a,b,c in random:
    copy_graph = copy.deepcopy(graph)
    ax = int(a//m); ay = int(a%m)
    bx = int(b//m); by = int(b%m)
    cx = int(c//m); cy = int(c%m)
    # print(ax,ay, bx, by, cx, cy)
    if (copy_graph[ax][ay]==0) & (copy_graph[bx][by]==0) & (copy_graph[cx][cy]==0):
        copy_graph[ax][ay] = 1
        copy_graph[bx][by] = 1
        copy_graph[cx][cy] = 1
        safety = max(safety,int(bfs(0,0)))

print(safety)
    