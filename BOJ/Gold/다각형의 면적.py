# https://www.acmicpc.net/problem/2166
# 신발끈 공식

import sys
input = sys.stdin.readline

n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]

answer = 0
for i in range(n):
    x1, y1 = points[i]
    x2, y2 = points[(i+1) % n]
    answer += x1 * y2 - y1 * x2

print((abs(answer) / 2))