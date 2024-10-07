# https://www.acmicpc.net/problem/1927

import sys
input = sys.stdin.readline
from heapq import heappush, heappop

n = int(input())
q = []

while n > 0:
    n -= 1
    x = int(input())
    if not x and q:
        print(heappop(q))
    elif not x and not q:
        print(0)
    else:
        heappush(q,x)