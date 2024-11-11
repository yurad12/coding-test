# https://www.acmicpc.net/problem/17143
import sys
input = sys.stdin.readline

R, C, M = map(int, input().split())
sharks = [list(map(int, input().split())) for _ in range(M)]

direc = [(0, 0), (-1, 0), (1, 0), (0, 1), (0, -1)]  # 위, 아래, 오, 왼
change = [0, 2, 1, 4, 3]

def move(sharks):
    new_positions = {}

    for i in range(len(sharks)):
        r, c, s, d, z = sharks[i]
        direction = direc[d]

        # 현재 방향 + 반대 방향 =  2 * (x-1) 패턴
        if d == 1 or d == 2:
            s %= (R - 1) * 2
        else:
            s %= (C - 1) * 2

        for _ in range(s):
            nr = r + direction[0]
            nc = c + direction[1]

            if nr < 1 or nr > R or nc < 1 or nc > C:
                d = change[d]
                direction = direc[d]
                nr = r + direction[0]
                nc = c + direction[1]

            r, c = nr, nc

        if (r, c) in new_positions:
            if new_positions[(r, c)][4] < z:
                new_positions[(r, c)] = (r, c, s, d, z)
        else:
            new_positions[(r, c)] = (r, c, s, d, z)

    return list(new_positions.values())

answer = 0
for j in range(1, C + 1):
    idx, r = -1, R + 1

    for i, shark in enumerate(sharks):
        if shark[1] == j and shark[0] < r:
            idx, r = i, shark[0]

    if idx > -1:
        answer += sharks[idx][4]
        sharks[idx] = sharks[-1]
        sharks.pop()
        
    sharks = move(sharks)

print(answer)