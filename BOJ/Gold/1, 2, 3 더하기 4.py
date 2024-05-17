# https://www.acmicpc.net/problem/15989

import sys
input = sys.stdin.readline

dp = [1] * 10001
for i in range(2, 10001):
    dp[i] += dp[i-2]

for i in range(3, 10001):
    dp[i] += dp[i-3]

t = int(input())
while t:
    t -= 1
    n = int(input())
    print("result:", dp[n])


'''
1, 2, 3
1 : 1 -> 1
2 : 1+1, 2 -> 2
3 : 1+1+1, 1+2, 3 -> 3
4 : 1+1+1+1, 1+1+2, 2+2, 1+3 -> 4
5 : 1+1+1+1+1, 1+1+1+2, 1+2+2, 1+1+3, 2+3 -> 5=2+3
6 : 1+1+1+1+1+1, 1+1+1+1+2, 1+1+2+2, 2+2+2, 1+1+1+3, 1+2+3, 3+3 -> 7=3+4

2> dp[2] = 2, dp[3] = 2, dp[4] = 3, dp[5] = 3
3>            dp[3] = 3, dp[4] = 4, dp[5] = 5
'''