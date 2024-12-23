# https://www.acmicpc.net/problem/14002
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp = [1] * N
prev = [-1] * N

for i in range(N):
    for j in range(i):
        if A[i] > A[j] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
            prev[i] = j

max_length = max(dp)
idx = dp.index(max_length)

answer = []
while idx != -1:
    answer.append(A[idx])
    idx = prev[idx]

print(len(answer))
print(*reversed(answer))