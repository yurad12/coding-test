# https://www.acmicpc.net/problem/14503

import sys
input = sys.stdin.readline

n, m = map(int,input().split())
x, y, d = map(int,input().split())
array = [list(map(int,input().split())) for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 0:북, 1:동, 2:남, 3:서
def rotate(now):
    next = (now + 3) % 4
    return next

# 주위 4칸 확인
def check(x,y):
    status = False
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or nx>=n or ny<0 or ny>=m:
            continue
        if array[nx][ny] == 0:
            status = True
    return status    

count = 0
while True:
    if array[x][y] == 0:
        array[x][y] = 2
        count += 1

    # 빈칸 확인
    if check(x,y) == True:
        while True:
            d = rotate(d)
            nx = x + dx[d]
            ny = y + dy[d]
            if array[nx][ny] == 0:
                x, y = nx, ny
                break
    else:
        nx = x - dx[d]
        ny = y - dy[d]
        if nx<0 or nx>=n or ny<0 or ny>=m:
            break
        if array[nx][ny] != 1:
            x, y = nx, ny
            continue
        break

print(count)
