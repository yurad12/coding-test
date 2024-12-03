# https://www.acmicpc.net/problem/10816

import sys
from bisect import bisect_right, bisect_left

n = int(sys.stdin.readline())
cards = list(map(int,sys.stdin.readline().split()))
cards.sort()
m = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))

for num in nums:
    left = bisect_left(cards, num)
    right = bisect_right(cards, num)
    print(right-left, end=' ')