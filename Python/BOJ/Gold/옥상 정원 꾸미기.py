# https://www.acmicpc.net/problem/6198
import sys
input = sys.stdin.readline

N = int(input())
H = [int(input()) for _ in range(N)]

dp = [0] * N
stack = [] # (index, value)
for i in range(N-1, -1, -1):
    count = 0
    while stack and stack[-1][1] < H[i]:
        count += dp[stack.pop()[0]]
        count += 1
    stack.append((i, H[i]))
    dp[i] = count

print(sum(dp))