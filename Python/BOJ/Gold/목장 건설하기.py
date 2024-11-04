# https://www.acmicpc.net/problem/14925
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(M)]

dp = [[0] * N for _ in range(M)]
answer = 0

for i in range(M):
    for j in range(N):
        if area[i][j] != 0:
            continue
        if i == 0 or j == 0:
            dp[i][j] = 1
        else:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        answer = max(answer, dp[i][j])

print(answer)
