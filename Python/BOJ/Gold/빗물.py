# https://www.acmicpc.net/problem/14719
# 양 옆이 자신보다 높은 블록인가?

import sys
input = sys.stdin.readline

h, w = map(int, input().split())
rain = list(map(int, input().split()))

result = 0
for i in range(1,w-1):
    left = max(rain[:i])
    right = max(rain[i+1:])
    temp = min(left, right)

    if rain[i] < temp:
        result += (temp-rain[i])

print(result)
