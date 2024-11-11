# https://www.acmicpc.net/problem/17521
import sys
input = sys.stdin.readline

n, w = map(int, input().split())
coins = [int(input()) for _ in range(n)]

answer = w
for i in range(n-1):
    if coins[i] < coins[i+1]:
        count = answer // coins[i]
        answer += count * (coins[i+1] - coins[i])

print(answer)