# https://www.acmicpc.net/problem/22866

import sys
input = sys.stdin.readline

N = int(input())
heights = list(map(int, input().split()))
INF = int(1e9)

# 건물 개수
counts = [0] * (N+1)
# [가까운 건물 번호, 가까운 건물 거리]
result = [[INF, INF] for _ in range(N+1)]

# 현재 빌딩을 기준으로 왼쪽에 볼 수 있는 건물
stack = []
for i in range(N):
    while stack and stack[-1][1] <= heights[i]:
        stack.pop()
    counts[i+1] += len(stack)

    if stack:
        dist = abs(stack[-1][0] - (i+1))
        if dist < result[i+1][1]:
            result[i+1][0], result[i+1][1] = stack[-1][0], dist
        elif dist == result[i+1][1] and stack[-1][0] < result[i+1][0]:
            result[i+1][0] = stack[-1][0]

    stack.append((i+1, heights[i]))

# 현재 빌딩을 기준으로 오른쪽에 볼 수 있는 건물
stack = []
for i in range(N-1,-1,-1):
    while stack and stack[-1][1] <= heights[i]:
        stack.pop()
    counts[i+1] += len(stack)

    if stack:
        dist = abs(stack[-1][0] - (i+1))
        if dist < result[i+1][1]:
            result[i+1][0], result[i+1][1] = stack[-1][0], dist
        elif dist == result[i+1][1] and stack[-1][0] < result[i+1][0]:
            result[i+1][0] = stack[-1][0]

    stack.append((i+1, heights[i]))    

for i in range(1, N+1):
    if counts[i]:
        print(counts[i], result[i][0])
    else:
        print(0)
