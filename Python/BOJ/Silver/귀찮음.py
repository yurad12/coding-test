# https://www.acmicpc.net/problem/16208
import sys
input = sys.stdin.readline
from heapq import heapify, heappush, heappop

N = int(input())
poles = list(map(int, input().split()))

heapify(poles)
answer = 0

while len(poles) > 1:
    a = heappop(poles)
    b = heappop(poles)
    answer += a * b
    heappush(poles, a+b)

print(answer)