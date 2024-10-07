# https://www.acmicpc.net/problem/18353

import sys

n = int(sys.stdin.readline())
soldiers = list(map(int,sys.stdin.readline().split()))
soldiers.reverse()
d = [1]*n

for i in range(1,n):
    for j in range(i):
        if soldiers[i] > soldiers[j]:
            d[i] = max(d[i],d[j]+1)
# print(d)
print(n-max(d))