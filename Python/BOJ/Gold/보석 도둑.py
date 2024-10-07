# https://www.acmicpc.net/problem/1202

import sys
input = sys.stdin.readline
from heapq import heappush, heappop

N, K = map(int, input().split())
jewelrys = [list(map(int, input().split())) for _ in range(N)]
bags = [int(input()) for _ in range(K)]

jewelrys.sort()
bags.sort()

q = []
answer = 0
i = 0
for bag in bags:
    while i < N and jewelrys[i][0] <= bag:
        heappush(q, -jewelrys[i][1])
        i += 1
    if q:
        answer -= heappop(q)

print(answer)
