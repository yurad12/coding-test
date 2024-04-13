# https://www.acmicpc.net/problem/15650
import sys
input = sys.stdin.readline

# 풀이1: 조합
from itertools import combinations

n, m = map(int, input().split())
combs = list(combinations(list(range(1,n+1)),m))
for comb in combs:
    for c in comb:
        print(c, end = ' ')
    print()

# 풀이2: 백트래킹
n, m = map(int, input().split())
nums = []
def dfs(start):
    if len(nums) == m:
        print(' '.join(map(str,nums)))
        return
    for i in range(start,n+1):
        if i not in nums:
            nums.append(i)
            dfs(i+1)
            nums.pop()
dfs(1)