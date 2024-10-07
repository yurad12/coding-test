# https://www.acmicpc.net/problem/2667

from collections import deque

n = int(input())
graph = [list(map(int,input())) for _ in range(n)]
# print(graph)

def bfs(graph,x,y):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    count = 1 # 단지 내의 집 수
    graph[x][y] += 1
    q = deque()
    q.append((x,y))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx<0) | (nx>=n) | (ny<0) | (ny>=n):
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] += 1
                q.append((nx,ny))
                count += 1
    return count

num = [bfs(graph,i,j) for i in range(n) for j in range(n) if graph[i][j]==1]            
print(len(num))
num.sort()
for i in num:
    print(i)