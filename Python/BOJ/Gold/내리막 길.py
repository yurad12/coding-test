# https://www.acmicpc.net/problem/1520
# dfs + dp

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

visited = [[-1] * N for _ in range(M)]

def dfs(x, y):
    if x == M-1 and y == N-1:
        return 1
    
    if visited[x][y] != -1:
        return visited[x][y]

    visited[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= M or ny < 0 or ny >= N:
            continue
        if board[x][y] > board[nx][ny]:
            visited[x][y] += dfs(nx, ny)
    
    return visited[x][y]


dfs(0,0)
print(visited[0][0])

