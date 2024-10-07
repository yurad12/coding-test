# https://www.acmicpc.net/problem/15686

import sys
input = sys.stdin.readline
from itertools import combinations

n, m = map(int,input().split())
array = [list(map(int,input().split())) for _ in range(n)]

house = []
chicken = []
for i in range(n):
    for j in range(n):
        if array[i][j] == 1:
            house.append((i,j))
        if array[i][j] == 2:
            chicken.append((i,j))

candidates = list(combinations(chicken,m))
result = 1e9
for candidate in candidates:
    temp = 0
    for x, y in house:
        dist = 1e9
        for c in range(len(candidate)):
            i, j = candidate[c]
            dist = min(dist, abs(x-i)+abs(y-j))
        temp += dist
    result = min(result,temp)
print(result)