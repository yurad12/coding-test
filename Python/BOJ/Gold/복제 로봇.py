# https://www.acmicpc.net/problem/1944
import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
maze = [list(input().strip()) for _ in range(N)]

nodes = []
for i in range(N):
    for j in range(N):
        if maze[i][j] == 'S' or maze[i][j] == 'K':
            nodes.append((i,j))

# 1. S, K 위치에서 다른 S, K까지 최단거리
dx = [-1,1,0,0]
dy = [0,0,-1,1]

q = deque()
edges = []

for i in range(M+1):
    x, y = nodes[i][0], nodes[i][1]
    q.append((x, y))
    dist = [[-1] * N for _ in range(N)]
    dist[x][y] = 0

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or nx >= N or ny < 0 or ny >= N or maze[nx][ny] == '1':
                continue
            if dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx,ny))

    for j in range(i+1, M+1):
        x, y = nodes[j][0], nodes[j][1]
        if dist[x][y] > 0:
            edges.append((dist[x][y], i, j))

# 2. MST로 연결되지 않은 노드 연결
# 3. 총 거리
def find(parent, x):
    if x != parent[x]:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

edges.sort()
answer, connected = 0, 0
parent = [i for i in range(M+1)]

for edge in edges:
    cost, a, b = edge
    if connected == M:
        break
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        connected += 1
        answer += cost

if connected == M:
    print(answer)
else:
    print(-1)