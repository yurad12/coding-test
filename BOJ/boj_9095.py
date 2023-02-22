# https://www.acmicpc.net/problem/9095

import sys
from itertools import product


c = int(sys.stdin.readline())
nums = [1,2,3]

def solution(n):
    count = 0

    for i in range(1,n+1):
        temp = list(product(nums,repeat=i))
        for t in temp:
            if sum(t) == n:
                count += 1
    print(count)

for _ in range(c):
    n = int(sys.stdin.readline())
    solution(n)