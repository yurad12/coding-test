# https://www.acmicpc.net/problem/1644
import sys
input = sys.stdin.readline
import math

N = int(input())
prime_numbers = [True] * (N+1)
for i in range(2, int(math.sqrt(N))+1):
    j = 2
    while i * j <= N:
        prime_numbers[i*j] = False
        j += 1

nums = [i for i in range(2, N+1) if prime_numbers[i]]

answer, now = 0, 0
start, end = 0, 0
while end <= len(nums):
    if now == N:
        answer += 1
        now -= nums[start]
        start += 1
    elif now < N:
        if end == len(nums):
            break
        now += nums[end]
        end += 1
    else:
        now -= nums[start]
        start += 1

print(answer)