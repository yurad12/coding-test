# https://www.acmicpc.net/problem/16946

import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def find_zero_group(x, y, visited, group, num):
    q = deque([(x,y)])
    count = 1
    visited[x][y] = 1

    while q:
        x, y = q.popleft()
        group[x][y] = num

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if not visited[nx][ny] and not graph[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx,ny))
                count += 1

    return count

def calculate_count(x, y, group, zeros):
    nums = set()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if group[nx][ny]:
            nums.add(group[nx][ny])
    
    count = 1
    for cnt in nums:
        count += zeros[cnt]
    
    return count % 10

# find zero group
visited = [[0] * M for _ in range(N)]
group = [[0] * M for _ in range(N)]
num = 1
zeros = {}

for i in range(N):
    for j in range(M):
        if not graph[i][j] and not visited[i][j]:
            count = find_zero_group(i, j, visited, group, num)
            zeros[num] = count
            num += 1

# find moving count
answer = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if graph[i][j]:
            answer[i][j] = calculate_count(i, j, group, zeros)

# print answer
for i in range(N):
    for j in range(M):
        print(answer[i][j], end='')
    print()