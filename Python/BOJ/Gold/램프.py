# https://www.acmicpc.net/problem/1034
import sys
input = sys.stdin.readline
from collections import Counter

N, M = map(int, input().split())
lamps = [input().strip() for _ in range(N)]
K = int(input())

lamps_count = Counter(lamps)
answer = 0

for i, count in lamps_count.items():
    zero = i.count('0')

    if zero <= K and (K - zero) % 2 == 0:
        answer = max(answer, count)

print(answer)
