# https://www.acmicpc.net/problem/1781

import sys
input = sys.stdin.readline
from heapq import heappush, heappop

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

data.sort()
hw = []
for deadline, ramen in data:
    heappush(hw, (ramen))
    if len(hw) > deadline:
        heappop(hw)

print(sum(hw))