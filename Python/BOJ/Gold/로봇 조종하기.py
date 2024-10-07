# https://www.acmicpc.net/problem/2169

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
mars = [list(map(int, input().split())) for _ in range(N)]

# top: row 0
for j in range(1,M):
    mars[0][j] += mars[0][j-1]

for i in range(1, N):
    # bottom ↓
    left, right =  [], []
    for j in range(M):
        value = mars[i][j] + mars[i-1][j]
        left.append(value)
        right.append(value)

    # right →
    for j in range(1, M):
        left[j] = max(left[j], left[j-1] + mars[i][j])
    
    # left ←
    for j in range(M-2, -1, -1):
        right[j] = max(right[j], right[j+1] + mars[i][j])

    # select
    for j in range(M):
        mars[i][j] = max(left[j], right[j])

print(mars[-1][-1])
