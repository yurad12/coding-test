# https://www.acmicpc.net/problem/15683
import sys
input = sys.stdin.readline
import copy

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

d = [(0,1), (0,-1), (1,0), (-1,0)]
rotate_dir = {1: [[0], [1], [2], [3]],
        2: [[0, 1], [2, 3]],
        3: [[0, 2], [0, 3], [1, 2], [1, 3]],
        4: [[0, 1, 2], [0, 1, 3], [2, 3, 0], [2, 3, 1]],
        5: [[0, 1, 2, 3]]}

def check(x, y, d, grid):
    while True:
        x += d[0]
        y += d[1]
        if x < 0 or x >= N or y < 0 or y >= M or grid[x][y] == 6:
            break
        if grid[x][y] == 0:
            grid[x][y] = '#'

def dfs(grid, count):
    global answer
    if count == len(cctv):
        min_value = 0
        for i in range(N):
            min_value += grid[i].count(0)
        answer = min(answer, min_value)
        return
    
    new_grid = copy.deepcopy(grid)
    x, y, num = cctv[count]
    for dir in rotate_dir[num]:
        for i in dir:
            check(x, y, d[i], new_grid)
        dfs(new_grid, count+1)
        new_grid = copy.deepcopy(grid)

cctv = []
for i in range(N):
    for j in range(M):
        if grid[i][j] in {1,2,3,4,5}:
            cctv.append((i, j, grid[i][j]))

answer = int(1e9)
dfs(grid, 0)
print(answer)