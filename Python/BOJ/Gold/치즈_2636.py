# https://www.acmicpc.net/problem/2636
import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    q = deque([(0,0)])
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    cheese = deque()

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny]:
                continue

            visited[nx][ny] = 1

            if not board[nx][ny]:
                q.append((nx,ny))
            else:
                cheese.append((nx,ny))
    
    return cheese


total = sum(sum(board[i]) for i in range(n))
time, count = 0, 0

while total:
    cheese = bfs()

    for x, y in cheese:
        board[x][y] = 0

    total -= len(cheese)
    time += 1
    count = len(cheese)

print(time)
print(count)