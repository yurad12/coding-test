# https://www.acmicpc.net/problem/3190
# 부호로 표시하면 index error, and로 표시하면 에러 안뜸

import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
array = [[0]*(n+1) for _ in range(n+1)]
for _ in range(k):
    a,b = map(int,input().split())
    array[a][b] = 1
cnt = int(input())
turn = []
for _ in range(cnt):
    x, c = input().split()
    turn.append((int(x),c))

# 동,서,남,북(시작기준) - 0,1,2,3
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def rotate(now,direc):
    if direc == 'L':
        now = (now - 1) % 4
    else:
        now = (now + 1) % 4
    
    return now

# 탐색
time = 0
x, y = 1, 1
array[x][y] = 2
now = 0
q = [(x,y)]
idx = 0 # 회전횟수

while True:
    # next x,y
    nx = x + dx[now]
    ny = y + dy[now]
    
    # check bump
    if 0<nx and nx<=n and 0<ny and ny<=n and array[nx][ny] != 2:
        # check snake and apple
        if array[nx][ny] == 0:
            array[nx][ny] = 2
            q.append((nx,ny))
            bx, by = q.pop(0)
            array[bx][by] = 0
        if array[nx][ny] == 1:
            array[nx][ny] = 2
            q.append((nx,ny))
    else:
        time += 1
        break
    
    x, y = nx, ny
    
    # count seconds, turn
    time += 1
    if idx < cnt and time == turn[idx][0]:
        now = rotate(now,turn[idx][1])
        idx += 1

print(time)