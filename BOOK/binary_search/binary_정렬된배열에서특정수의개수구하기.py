import sys
from bisect import bisect_right, bisect_left

n, x = map(int,sys.stdin.readline().split())
nums = list(map(int,sys.stdin.readline().split()))

left = bisect_left(nums, x)
right = bisect_right(nums, x)

if right-left == 0:
    print(-1)
else:
    print(right-left)