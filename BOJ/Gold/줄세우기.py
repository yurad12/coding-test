# https://www.acmicpc.net/problem/2631
'''
1. 가장 긴 증가하는 부분 수열을 구하기
2. dp[i] = max(dp[i], dp[j]+1)
'''

import sys
input = sys.stdin.readline

N = int(input())
nums = [0] + list(int(input()) for _ in range(N))

dp = [1] * (N+1)
for i in range(1, N+1):
    for j in range(1, i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(N - max(dp))
