import sys
input = sys.stdin.readline

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