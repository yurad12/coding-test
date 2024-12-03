# https://www.acmicpc.net/problem/2293

import sys
input = sys.stdin.readline

n, k = map(int,input().split())
coins = list(int(input()) for _ in range(n))
d = [0] * (k+1)
d[0] = 1

for coin in coins:
    for j in range(coin,k+1):
        d[j] += d[j-coin]

print(d[k])