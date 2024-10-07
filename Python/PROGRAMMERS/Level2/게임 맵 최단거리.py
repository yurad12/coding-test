'''
https://school.programmers.co.kr/learn/courses/30/lessons/1844

bfs로 (0,0)부터 탐색하면서 거리 갱신
'''

from collections import deque

def solution(maps):
    answer = -1
    n, m = len(maps), len(maps[0])
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    visited = [[0]*m for _ in range(n)]
        
    q = deque([(0,0)])
    visited[0][0] = 1
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny] or not maps[nx][ny]:
                continue
            q.append((nx,ny))
            visited[nx][ny] = 1
            if maps[nx][ny] == 1:
                maps[nx][ny] += maps[x][y]
            elif maps[nx][ny] > 1:
                maps[nx][ny] = min(maps[nx][ny], maps[nx][ny]+maps[x][y])
    if maps[n-1][m-1] > 1:
        answer = maps[n-1][m-1]
    return answer
