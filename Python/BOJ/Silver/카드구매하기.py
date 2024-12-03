# https://www.acmicpc.net/problem/11052

import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int,input().split()))
d = [0] * (n+1)

for i in range(1,n+1):
    for j in range(1,i+1):
        d[i] = max(d[i], d[i-j] + cards[j-1])
    # print(d)
print(d[n])