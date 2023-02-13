# https://www.acmicpc.net/problem/14501

import sys

n = int(sys.stdin.readline())
tp = []
for _ in range(n):
    ti, pi = map(int,sys.stdin.readline().split())
    tp.append([ti,pi])

# 점화식: d[i] = max(p[i] + d[t[i]+i],max_value)
d = [0]*1000
max_value = 0
for i in range(n-1,-1,-1):
    day = tp[i][0] + i
    if day <= n: 
        d[i] = max(tp[i][1]+d[day], max_value)
        max_value = d[i]
        # print('1',d[:n+1])
    else:
        d[i] = max_value
        # print('2',d[:n+1])
print(max_value)