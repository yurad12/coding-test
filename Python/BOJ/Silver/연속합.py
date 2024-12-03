# https://www.acmicpc.net/problem/1912

import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int,input().split()))
d = [-1001] * (n+1)
d[0] = array[0]

for i in range(1,n):
    temp = d[i-1] + array[i]
    if temp > array[i]:
        d[i] = temp
    else:
        d[i] = array[i]
print(max(d))