# https://www.acmicpc.net/problem/2531

import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(n)]

sushi += sushi
answer = 0

for i in range(n+k):
    dishes = set(sushi[i:i+k])
    count = len(dishes)
    if c not in dishes:
        count += 1
    answer = max(answer, count)

print(answer)

