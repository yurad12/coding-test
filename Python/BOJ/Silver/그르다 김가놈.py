# https://www.acmicpc.net/problem/18113
import sys
input = sys.stdin.readline

N, K, M = map(int, input().split())
gimbap = []

for _ in range(N):
    x = int(input())

    if x > 2 * K:
        gimbap.append(x - 2 * K)
    elif K < x and x < 2 * K:
        gimbap.append(x - K)

answer = -1
if not gimbap:
    print(answer)
    sys.exit()

start, end = 1, max(gimbap)

while start <= end:
    mid = (start + end) // 2

    total = 0
    for x in gimbap:
        total += x // mid
    
    if total < M:
        end = mid - 1
    else:
        start = mid + 1
        answer = mid

print(answer)