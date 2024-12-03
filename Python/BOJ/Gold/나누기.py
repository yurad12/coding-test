# https://www.acmicpc.net/problem/21757
import sys
input = sys.stdin.readline
from itertools import accumulate

N = int(input())
nums = list(map(int, input().split()))

total = sum(nums)
if total % 4 != 0:
    print(0)
    sys.exit()

target = total // 4
prefix_sum = list(accumulate(nums))

cnt1, cnt2 = 0, 0
answer = 0

for i in range(N-1):
    if prefix_sum[i] == 3 * target:
        answer += cnt2
    
    if prefix_sum[i] == 2 * target:
        cnt2 += cnt1
    
    if prefix_sum[i] == target:
        cnt1 += 1

print(answer)
