# https://www.acmicpc.net/problem/7568

import sys
input = sys.stdin.readline

n = int(input())
bodies = [list(map(int,input().split())) for _ in range(n)]
result = [1] * (n)

for i in range(n):
    x1, y1 = bodies[i]
    for j in range(n):
        x2, y2 = bodies[j]
        if i == j:
            continue
        if x1 < x2 and y1 < y2:
            result[i] += 1

for res in result:
    print(res, end=' ')
print()