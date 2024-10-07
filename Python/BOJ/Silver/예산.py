# https://www.acmicpc.net/problem/2512

import sys
input = sys.stdin.readline

n = int(input())
budgets = list(map(int, input().split()))
m = int(input())

start, end = 0, max(budgets)
result = 0
while start <= end:
    mid = (start+end) // 2
    total = 0
    for b in budgets:
        if b < mid:
            total += b
        else:
            total += mid
    
    if total > m:
        end = mid-1
    else:
        start = mid+1
        result = mid

print(result)
