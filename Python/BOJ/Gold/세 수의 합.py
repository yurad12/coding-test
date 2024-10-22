# https://www.acmicpc.net/problem/2295
# U[k] = U[x] + U[y] + U[z]
# U[k] = U[l] + U[z]
import sys
input = sys.stdin.readline

N = int(input())
U = [int(input()) for _ in range(N)]

U.sort()
sum_set = set()
for x in range(N):
    for y in range(N):
        sum_set.add(U[x] + U[y])

answer = 0
for k in range(N-1, -1, -1):
    for z in range(k):
        if U[k] - U[z] in sum_set:
            answer = U[k]
            break
    if answer:
        break

print(answer)