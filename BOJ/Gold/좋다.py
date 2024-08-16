# https://www.acmicpc.net/problem/1027

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
nums.sort()

answer = 0
for i in range(n):
    target = nums[i]
    a, b = 0, n-1
    while a < b:
        if a == i:
            a += 1
            continue
        elif b == i:
            b -= 1
            continue
        
        if nums[a] + nums[b] == target:
            answer += 1
            break
        elif nums[a] + nums[b] < target:
            a += 1
        else:
            b -= 1

print(answer)
