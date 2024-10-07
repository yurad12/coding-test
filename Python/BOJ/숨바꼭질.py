# https://www.acmicpc.net/problem/1697

import sys

n, k = map(int,sys.stdin.readline().split())
inf = int(1e9)
d = [abs(i-n) for i in range(100001)]
d[n] = 0

for c in range(2):
    if n == k or k == 0:
        break
    for i in range(100001):
        if i-1 >= 0:
            d[i-1] = min(d[i-1],d[i]+1)
        if i+1 < 100001:
            d[i+1] = min(d[i+1], d[i]+1)
        if i*2 < 100001:
            d[i*2] = min(d[i*2], d[i]+1)

print(d[k])