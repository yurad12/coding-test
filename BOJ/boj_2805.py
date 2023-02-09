# https://www.acmicpc.net/problem/2805

import sys

n, m = map(int,sys.stdin.readline().split())
trees = list(map(int,sys.stdin.readline().split()))

start = 0
end = max(trees)

while start <= end:
    total = 0
    mid = (start+end)//2

    for t in trees:
        if t > mid:
            total += (t-mid)
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
print(result)