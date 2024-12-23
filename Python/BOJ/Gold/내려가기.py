# https://www.acmicpc.net/problem/2096
import sys
input = sys.stdin.readline

N = int(input())

dp_max = []
dp_min = []

for i in range(N):
    board = list(map(int, input().split()))

    if i == 0:
        dp_max = board[:]
        dp_min = board[:]
        continue

    dp_max = [board[0] + max(dp_max[0], dp_max[1]),
             board[1] + max(dp_max[0], dp_max[1], dp_max[2]),
             board[2] + max(dp_max[1], dp_max[2])]

    dp_min = [board[0] + min(dp_min[0], dp_min[1]),
             board[1] + min(dp_min[0], dp_min[1], dp_min[2]),
             board[2] + min(dp_min[1], dp_min[2])]

print(max(dp_max), min(dp_min))