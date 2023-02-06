# https://www.acmicpc.net/problem/16234
# l이상 r이하일 때 연합, 인구이동
import sys
from collections import deque

n, l, r = map(int,sys.stdin.readline().split())
matrix = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def solution(x,y,visited):
    visited[x][y] = True
    united = deque() # 연합 노드들
    united.append((x,y))
    q = deque()
    q.append((x,y))
    uni_cnt = 1
    sum = matrix[x][y]

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # print(nx,ny)
            if (0 <= nx < n) and (0 <= ny < n) and (visited[nx][ny]==False):
                if l <= abs(matrix[x][y]-matrix[nx][ny]) <= r:
                    visited[nx][ny] = True
                    united.append((nx,ny))
                    uni_cnt += 1
                    sum += matrix[nx][ny]
                    q.append((nx,ny))
                    # print('okay')
        # print(visited)
    # print(q)
    for a,b in united:
        matrix[a][b] = int(sum/uni_cnt)
    # print(matrix)
    return uni_cnt

result = 0
while True:
    flag = 0
    visited = [[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                # print(visited)
                solution(i,j,visited) 
                flag += 1    
    if flag == n*n:
        break
    result += 1
# print(matrix)
print(result)