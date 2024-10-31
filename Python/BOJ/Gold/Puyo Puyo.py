# https://www.acmicpc.net/problem/11559
import sys
input = sys.stdin.readline
from collections import deque

N, M = 12, 6
fields = [list(input().strip()) for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def find(N, M, fields):
    remove_set = []
    visited = [[0] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if fields[i][j] == '.' or visited[i][j]:
                continue

            q = deque([(i,j)])
            connected = {(i,j)}

            while q:
                x, y = q.popleft()
                
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if nx < 0 or nx >= N or ny < 0 or ny >= M or (nx, ny) in connected:
                        continue
                    if fields[x][y] == fields[nx][ny]:
                        q.append((nx,ny))
                        connected.add((nx,ny))
            
            if len(connected) >= 4:
                remove_set.append(connected)
                for i, j in connected:
                    visited[i][j] = 1
    
    return remove_set


def explode(fields, remove_set):
    for now_set in remove_set:
        for i, j in now_set:
            fields[i][j] = '.'

def drop(N, M, fields):
    for j in range(M):
        now = N - 1
        for i in range(N-1, -1, -1):
            if fields[i][j] != '.':
                fields[now][j] = fields[i][j]
                if now != i:
                    fields[i][j] = '.'
                now -= 1

answer = 0
while True:
    remove_set = find(N, M, fields)
    if not remove_set:
        break
    explode(fields, remove_set)
    drop(N, M, fields)
    answer += 1

print(answer)