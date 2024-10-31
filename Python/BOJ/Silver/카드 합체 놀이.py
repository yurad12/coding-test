# https://www.acmicpc.net/problem/15903
import sys
input = sys.stdin.readline
from heapq import heappush, heappop

n, m = map(int, input().split())
cards = list(map(int, input().split()))
q = []
for c in cards:
    heappush(q, c)

for _ in range(m):
    sum_value = heappop(q) + heappop(q)
    heappush(q, sum_value)
    heappush(q, sum_value)

print(sum(q))