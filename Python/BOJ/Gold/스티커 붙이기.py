# https://www.acmicpc.net/problem/18808
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

def rotate(sticker, r, c):
    rotated = [[0] * r for _ in range(c)]
    for i in range(r):
        for j in range(c):
            rotated[j][r-i-1] = sticker[i][j]
    return rotated

def check(sticker, r, c, x, y):
    for i in range(r):
        for j in range(c):
            if sticker[i][j]:
                if x + i >= N or y + j >= M or laptop[x+i][y+j] == 1:
                    return False
    return True

def attach(sticker, r, c, x, y):
    for i in range(r):
        for j in range(c):
            if sticker[i][j] == 1:
                laptop[x+i][y+j] = 1

laptop = [[0] * M for _ in range(N)]
for _ in range(K):
    R, C = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(R)]
    placed = False
    for _ in range(4):
        for x in range(N-R+1):
            for y in range(M-C+1):
                if check(sticker, R, C, x, y):
                    attach(sticker, R, C, x, y)
                    placed = True
                    break
            if placed:
                break
        if placed:
            break
        sticker = rotate(sticker, R, C)
        R, C = C, R

answer = sum(i.count(1) for i in laptop)
print(answer)