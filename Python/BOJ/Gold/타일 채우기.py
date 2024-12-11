# https://www.acmicpc.net/problem/2133
import sys
input = sys.stdin.readline

N = int(input())

if N % 2 != 0:
    print(0)
    sys.exit()

dp = [0] * (N+1)
dp[2] = 3

for i in range(4, N+1, 2):
    dp[i] = dp[i-2] * 3 + 2
    for j in range(2, i-2, 2):
        dp[i] += 2 * dp[j]

print(dp[N])