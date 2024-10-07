# https://school.programmers.co.kr/learn/courses/30/lessons/67259

from collections import deque

def solution(board):
    n = len(board)
    route = [[[int(1e9)] * 4 for _ in range(n)] for _ in range(n)]
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    q = deque([(0,0,-1,0)]) # x, y, d, cost
    for i in range(4):
        route[0][0][i] = 0
    
    while q:
        x, y, d, c = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n or board[nx][ny]:
                continue
            
            if d == i or d == -1:
                cost = c + 100
            else:
                cost = c + 600
            
            if cost < route[nx][ny][i]:
                route[nx][ny][i] = cost
                q.append((nx,ny,i,cost))

    answer = min(route[n-1][n-1])
    return answer