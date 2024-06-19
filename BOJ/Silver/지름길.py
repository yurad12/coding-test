# https://www.acmicpc.net/problem/1446

import sys
input = sys.stdin.readline

n, d = map(int, input().split())
shortcuts = [list(map(int, input().split())) for _ in range(n)]

shortcuts.sort(key = lambda x: x[1])

dp = [int(1e9)] * (10001)
dp[0] = 0
idx = 0

for i in range(1,d+1):
    while idx < n and shortcuts[idx][1] == i:
        start, end, dist = shortcuts[idx]
        dp[end] = min(dp[end], dp[start]+dist)
        idx += 1
    dp[i] = min(dp[i], dp[i-1]+1)

print(dp[d])
