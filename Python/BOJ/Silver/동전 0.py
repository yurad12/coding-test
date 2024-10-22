# https://www.acmicpc.net/problem/11047
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]

A.sort(reverse=True)
answer = 0
for a in A:
    if K >= a:
        answer += (K // a)
        K %= a

print(answer)