# https://www.acmicpc.net/problem/9251
import sys
input = sys.stdin.readline

X = input().strip()
Y = input().strip()

m, n = len(X), len(Y)
dp = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, m+1):
    for j in range(1, n+1):
        if X[i-1] == Y[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

answer = dp[m][n]
print(answer)