# https://www.acmicpc.net/problem/14658

import sys
input = sys.stdin.readline

n, m, l, k = map(int, input().split())
meteors = [list(map(int, input().split())) for _ in range(k)]

answer = 0
for x1, y1 in meteors:
    for x2, y2 in meteors:
        x_left, x_right = x1, x1 + l
        y_top, y_bottom = y2 + l, y2
        
        count = 0
        for x, y in meteors:
            if x_left <= x <= x_right and y_bottom <= y <= y_top:
                count += 1
        
        answer = max(answer, count)

print(k - answer)


