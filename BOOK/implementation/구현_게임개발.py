import sys
input = sys.stdin.readline

### solution1
n, m = map(int,input().split())
x, y, d = map(int,input().split())
array = [list(map(int,input().split())) for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]
visited = [[False]*m for _ in range(n)]
count = 1

# direction 1
def rotate(d):
    if d == 0:
        d = 3
    elif d == 1:
        d = 0
    elif d == 2:
        d = 1
    elif d == 3:
        d = 2
    return d

turn = 0
visited[x][y] = True

while True:
    # direction 2
    d = rotate(d)
    nx = x + dx[d]
    ny = y + dy[d]
    if (nx<0) | (nx>=n) | (ny<0) | (ny>=m):
        continue
    if (visited[nx][ny] == False) & (array[nx][ny] == 0):
        visited[nx][ny] = True
        # print(x,y,'>>>',nx,ny, '>>',d)
        x, y = nx, ny
        count += 1
        turn = 0
    else:
        # direction 3
        if turn == 4:
            x -= dx[d]
            y -= dy[d]
            visited[x][y] = True
            turn = 0
            if array[x][y] == 1:
                break
        turn += 1

print(count)


### solution2
n, m = map(int,input().split())
x, y, d = map(int, input().split())
gmap = [list(map(int,input().split())) for _ in range(n)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 1: sea, 0: land, -1: not visited land
answer = 0
while True:

    # 네 방향 칸 확인
    count = 0
    for i in range(4):
        cx = x + dx[i]
        cy = y + dy[i]
        if cx < 0 or cx >= n or cy < 0 or cy >= m:
            count += 1
            continue
        if gmap[cx][cy]:
            count += 1
    
    # 네 방향 확인 결과
    if count == 4:
        cd = (d+2) % 4
        cx = x + dx[cd]
        cy = y + dy[cd]
        if gmap[cx][cd] == 1 or cx < 0 or cx >= n or cy < 0 or cy >= m:
            break
        x, y = cx, cy
        continue

    # 왼쪽 방향 회전: (현재방향+3)%4 = (다음방향)
    nd = (d+3) % 4

    # 다음 칸 좌표
    nx = x + dx[nd]
    ny = y + dy[nd]

    # 왼쪽 방향 칸 방문 여부 확인
    if nx < 0 or nx >= n or ny < 0 or ny >= m or gmap[nx][ny] == -1 or gmap[nx][ny] == 1:
        d = nd
    elif not gmap[nx][ny]:
        gmap[nx][ny] = -1
        x, y, d = nx, ny, nd
        answer += 1

print(answer)