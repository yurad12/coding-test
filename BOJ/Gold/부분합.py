# https://www.acmicpc.net/problem/1806

import sys
input = sys.stdin.readline

N, S = map(int, input().split())
nums = list(map(int, input().split()))
INF = int(1e9)

prefix_sum = [0] * N
prefix_sum[0] = nums[0]
for i in range(1,N):
    prefix_sum[i] = prefix_sum[i-1] + nums[i]

answer = INF
left, right = 0, 0
current_sum = 0
while right < N:
    current_sum += nums[right]
    right += 1

    while current_sum >= S:
        answer = min(answer, right - left)
        current_sum -= nums[left]
        left += 1

if answer == INF:
    print(0)
else:
    print(answer)
