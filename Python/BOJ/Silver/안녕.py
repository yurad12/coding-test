# https://www.acmicpc.net/problem/1535
import sys
input = sys.stdin.readline

N = int(input())
stamina = list(map(int, input().split()))
delight = list(map(int, input().split()))

dp = [0] * 101
for i in range(N):
    s = stamina[i]
    d = delight[i]
    for j in range(99, s-1, -1):
        dp[j] = max(dp[j], dp[j-s] + d)

print(max(dp))