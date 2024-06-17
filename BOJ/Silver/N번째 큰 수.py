# https://www.acmicpc.net/problem/2075

import sys
input = sys.stdin.readline
from heapq import heappush, heapreplace

n = int(input())
numbers = []
for _ in range(n):
    data = list(map(int, input().split()))
    for num in data:
        if len(numbers) < n:
            heappush(numbers, num)
        else:
            if num > numbers[0]:
                heapreplace(numbers, num)

print(numbers[0])
