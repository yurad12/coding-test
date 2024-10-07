# https://www.acmicpc.net/problem/1863
# 1. x좌표 순서대로 살펴보면서 y가 낮아질 때, 건물 끝남
# 2. y가 높아질 때, 건물 시작

import sys
input = sys.stdin.readline

n = int(input())
lines = [list(map(int, input().split())) for _ in range(n)]

stack = [0]
answer = 0

for x, y in lines:
    # prev_y > current_y
    if stack and stack[-1] > y:
        while stack[-1] > y:
            stack.pop()
    # prev_y < current_y
    if stack and stack[-1] < y:
        stack.append(y)
        answer += 1

print(answer)

