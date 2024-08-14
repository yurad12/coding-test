# https://www.acmicpc.net/problem/3079

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
tables = list(int(input()) for _ in range(N))
INF = float('inf')

start, end = 1, max(tables) * M
answer = INF

while start <= end:
    mid = (start + end) // 2
    people = 0

    # 몇 명 수용할 수 있는지 확인
    for time in tables:
        people += mid // time

    if people < M:
        start = mid + 1
    else:
        answer = mid
        end = mid - 1

print(answer)
