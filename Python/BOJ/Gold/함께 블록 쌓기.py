# https://www.acmicpc.net/problem/18427
import sys
input = sys.stdin.readline

N, M, H = map(int, input().split())
blocks = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (H+1) for _ in range(N+1)]
dp[0][0] = 1
for i in range(1, N+1):
    dp[i] = dp[i-1][:]
    for h in blocks[i-1]:
        for j in range(H, h-1, -1):
            dp[i][j] = (dp[i][j] + dp[i-1][j-h]) % 10007

print(dp[N][H])