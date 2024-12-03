# https://www.acmicpc.net/problem/1025
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]
answer = -1

# 행, 열 선택 -> 공차 선택 -> 완전제곱수되는지 확인
for x in range(N):
    for y in range(M):
        for dx in range(-N, N):
            for dy in range(-M, M):
                if dx == 0 and dy == 0:
                    continue
                
                s = ''
                i, j = x, y
                while 0 <= i < N and 0 <= j < M:
                    s += board[i][j]
                    if int(int(s) ** 0.5) ** 2 == int(s):
                        answer = max(answer, int(s))
                    i += dx
                    j += dy

print(answer)
