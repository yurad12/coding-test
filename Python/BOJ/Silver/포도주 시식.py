# https://www.acmicpc.net/problem/2156
import sys
input = sys.stdin.readline

n = int(input())
A = [int(input()) for _ in range(n)]

dp = [0] * n

dp[0] = A[0]
if n > 1:
    dp[1] = A[0] + A[1]
if n > 2:
    dp[2] = max(A[2] + A[1], A[2] + A[0], dp[1])
for i in range(3, n):
    dp[i] = max(A[i] + A[i-1] + dp[i-3],
                A[i] + dp[i-2],
                dp[i-1])

print(dp[-1])