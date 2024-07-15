# https://www.acmicpc.net/problem/1987

import sys
input = sys.stdin.readline

R, C = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited = {}

def dfs(x, y, count, path):
    global answer
    if (x,y,path) in visited and visited[(x,y,path)] >= count:
        return
    
    visited[(x,y,path)] = count
    answer = max(answer, count)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            continue
        new_path = 1 << (ord(board[nx][ny]) - ord('A'))
        if not (path & new_path):
            dfs(nx, ny, count+1, path | new_path)

answer = 0
path = 1 << (ord(board[0][0]) - ord('A'))

dfs(0, 0, 1, path)

print(answer)

