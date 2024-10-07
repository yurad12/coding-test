# https://www.acmicpc.net/problem/11758

import sys
input = sys.stdin.readline

points = [list(map(int, input().split())) for _ in range(3)]

x1, y1 = points[0]
x2, y2 = points[1]
x3, y3 = points[2]
area = (x1*y2 + x2*y3 + x3*y1) - (x2*y1 + x3*y2 + x1*y3)

if area == 0:
    print(0)
elif area > 0:
    print(1)
else:
    print(-1)
