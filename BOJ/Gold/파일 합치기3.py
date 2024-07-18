# https://www.acmicpc.net/problem/13975

import sys
input = sys.stdin.readline
from heapq import heappush, heappop

T = int(input())
for _ in range(T):
    K = int(input())
    files = list(map(int, input().split()))
    q = []
    for file in files:
        heappush(q, file)

    answer = 0
    while len(q) > 1:
        a = heappop(q)
        b = heappop(q)
        answer += (a+b)
        heappush(q, a+b)
    
    print(answer)
