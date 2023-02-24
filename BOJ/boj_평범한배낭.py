# https://www.acmicpc.net/problem/12865

import sys
input = sys.stdin.readline

n, k = map(int,input().split())
d = [0] * (k+1)

for _ in range(n):
    weight, value = map(int,input().split())
    for j in range(k, weight-1, -1):
        d[j] = max(d[j],d[j-weight]+value)

print(d[-1])