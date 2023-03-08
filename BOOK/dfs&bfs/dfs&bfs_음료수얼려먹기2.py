from collections import deque

n, m = map(int,input().split())
frame = [list(map(int,input())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if frame[nx][ny]==0 and visited[nx][ny]==False:
                visited[nx][ny] = True
                q.append((nx,ny))

count = 0
for i in range(n):
    for j in range(m):
        if frame[i][j]==0 and visited[i][j]==False:
            bfs(i,j)
            count += 1
print(count)