# https://www.acmicpc.net/problem/14499
import sys
input = sys.stdin.readline

N, M, x, y, K = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
commands = list(map(int, input().split()))

# 동 서 북 남
rolls = {
    1: [3, 1, 0, 5, 4, 2],
    2: [2, 1, 5, 0, 4, 3],
    3: [4, 0, 2, 3, 5, 1],
    4: [1, 5, 2, 3, 0, 4]
}
def roll(dir):
    new_dice = dice[:]
    for i, j in enumerate(rolls[dir]):
        dice[i] = new_dice[j]

dx = [0,0,-1,1]
dy = [1,-1,0,0]
dice = [0] * 6

for c in commands:
    nx = x + dx[c-1]
    ny = y + dy[c-1]
    if nx < 0 or nx >= N or ny < 0 or ny >= M:
        continue

    x, y = nx, ny
    roll(c)
    if maps[x][y] == 0:
        maps[x][y] = dice[5]
    else:
        dice[5] = maps[x][y]
        maps[x][y] = 0
    print(dice[0])


'''
  2
4 1 3
  5
  6
      123456
1. 동: 421653
2. 서: 326154
3. 북: 513462
4. 남: 263415
'''