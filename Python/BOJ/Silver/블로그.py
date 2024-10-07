# https://www.acmicpc.net/problem/21921

import sys
input = sys.stdin.readline

n, x = map(int, input().split())
visitors = list(map(int, input().split()))

dp = [0] * n
result = 0

for i in range(n):
    result += visitors[i]
    if i-x >= 0:
        result -= visitors[i-x]
    dp[i] = result

term, answer = 1, 0
for i in range(n):
    if dp[i] > answer:
        answer = dp[i]
        term = 1
    elif dp[i] == answer:
        term += 1

if not result:
    print("SAD")
else:
    print(answer)
    print(term)