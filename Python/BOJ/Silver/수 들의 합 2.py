# https://www.acmicpc.net/problem/2003
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

left, right = 0, 0
answer, now = 0, 0
while right <= N:
    if now < M:
        if right == N:
            break
        now += nums[right]
        right += 1
    else:
        if now == M:
            answer += 1
        now -= nums[left]
        left += 1

print(answer)
