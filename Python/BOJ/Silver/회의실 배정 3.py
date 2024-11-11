# https://www.acmicpc.net/problem/19622
import sys
input = sys.stdin.readline

N = int(input())
meeting = [list(map(int, input().split())) for i in range(N)]
meeting.sort()

dp = [0] * N
dp[0] = meeting[0][2]
for i in range(1, N):
    dp[i] = max(dp[i-1], dp[i-2] + meeting[i][2])

print(dp[-1])