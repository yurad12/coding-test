# https://www.acmicpc.net/problem/1941
import sys
input = sys.stdin.readline
from collections import deque

graph = [input().rstrip() for _ in range(5)]
answer = 0
visited = [[False]*5 for _ in range(5)]
ps = []

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def check():
    q = deque()
    q.append(ps[0])
    visited = [[-1]*5 for _ in range(5)]
    for p in ps:
        visited[p[0]][p[1]] = 0
    visited[ps[0][0]][ps[0][1]] = 1
    jointed = 1

    while q:
        x, y = q.popleft()
    
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
                continue
            if not visited[nx][ny]:
                jointed += 1
                visited[nx][ny] = 1
                q.append((nx,ny))
    if jointed == 7:
        return True
    return False

def dfs(n,cnt,ycnt):
    global answer

    if ycnt > 3:
        return
    if cnt == 7:
        if check():
            answer += 1
        return
    
    for i in range(n, 25):
        x = i // 5
        y = i % 5
        ps.append((x,y))
        dfs(i+1, cnt+1, ycnt+int(graph[x][y]=="Y"))
        ps.pop()

dfs(0,0,0)
print(answer)
