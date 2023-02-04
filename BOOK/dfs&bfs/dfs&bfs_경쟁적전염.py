# https://www.acmicpc.net/problem/18405
import sys
from collections import deque

n, k = map(int,sys.stdin.readline().split())
matrix = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
sec, row, col = map(int,sys.stdin.readline().split())
dx = [-1,1,0,0]
dy = [0,0,-1,1]
virus = []
for i in range(n):
    for j in range(n):
        if matrix[i][j]!=0:
            virus.append((i,j,matrix[i][j],0))
virus = sorted(virus,key = lambda x:x[2])
# print(virus)
def bfs(matrix,sec,row,col):
    queue = deque()
    for a,b,v,s in virus:
        queue.append((a,b,s))
    while queue:
        x, y, s = queue.popleft()
        # print(x, y, s)
        if (s == sec):
            result = matrix[row-1][col-1]
            # print('stop')
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx<0) | (nx>=n) | (ny<0) | (ny>=n):
                continue
            if matrix[nx][ny] == 0:
                matrix[nx][ny] = matrix[x][y]
                queue.append((nx,ny,s+1))
    result = matrix[row-1][col-1]
    return result

print(bfs(matrix,sec,row,col))