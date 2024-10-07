# https://www.acmicpc.net/problem/3687
'''
2-1,1
3-7,7
4-4,4
5-2,71
6-6,111
7-8,711
8-10,1111
9-18,7111
10-22,11111
'''

import sys
input = sys.stdin.readline

n = int(input())
nums = list(int(input()) for _ in range(n))

dp = [float('inf')] * 101
matchsticks = ['', '', 1, 7, 4, 2, 6, 8]
for i in range(2,8):
    dp[i] = matchsticks[i]

for i in range(8,101):
    for j in range(2, i-1):
        dp[i] = min(dp[i], int(str(dp[j]) + str(dp[i-j])))
        if j == 6:
            dp[i] = min(dp[i], int(str(dp[i-j])+'0'))

for num in nums:
    min_num = dp[num]
    max_num = '1' * (num//2)
    if num % 2:
        max_num = '7' + max_num[1:]

    print(min_num, max_num)