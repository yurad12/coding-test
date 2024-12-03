# https://www.acmicpc.net/problem/1022
import sys
input = sys.stdin.readline

r1, c1, r2, c2 = map(int, input().split())

n, m = r2 - r1 + 1, c2 - c1 + 1
graph = [[0] * m for _ in range(n)]

# 오, 위, 왼, 아래
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

x, y = 0, 0
num = 1
dir_idx = 0
count = 1

value = 0
total = n * m

while total > 0:
    for _ in range(2): # 2번 방향 변경 후에 길이가 1길어짐
        for _ in range(count):
            if r1 <= x <= r2 and c1 <= y <= c2:
                graph[x-r1][y-c1] = num
                value = num
                total -= 1
            
            x += dx[dir_idx]
            y += dy[dir_idx]
            num += 1

        dir_idx = (dir_idx + 1) % 4
    count += 1

max_length = len(str(value))

for i in range(n):
    for j in range(m):
        print(str(graph[i][j]).rjust(max_length), end = ' ')
    print()