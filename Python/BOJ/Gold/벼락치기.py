# https://www.acmicpc.net/problem/14728
import sys
input = sys.stdin.readline

N, T = map(int, input().split())
chapters = [list(map(int, input().split())) for _ in range(N)]

dp = [0] * 10001
for k, s in chapters:
    for i in range(T, k-1, -1):
        dp[i] = max(dp[i], dp[i-k] + s)

print(max(dp))