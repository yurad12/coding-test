# https://www.acmicpc.net/problem/1932

import sys

n = int(sys.stdin.readline())
ta = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
d = [[0]*(i+1) for i in range(n)]
d[0][0] = ta[0][0]

for r in range(1,n): # 2
    for c in range(r+1): # 0
        if c == 0:
            d[r][c] = ta[r][c] + d[r-1][c]
        elif c == r:
            d[r][c] = ta[r][c] + d[r-1][c-1]
        else:
            d[r][c] = ta[r][c] + max(d[r-1][c-1],d[r-1][c])
    # print(d)
print(max(d[n-1]))