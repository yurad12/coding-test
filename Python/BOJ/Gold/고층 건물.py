# https://www.acmicpc.net/problem/1027

import sys
input = sys.stdin.readline

N = int(input())
buildings = list(map(int, input().split()))

def get_gradient(x1, y1, x2, y2):
    return (y2-y1) / (x2-x1)

answer = 0
for x1, y1 in enumerate(buildings):
    count = 0

    # left
    min_gradient = float('inf')
    for x2 in range(x1-1,-1,-1):
        y2 = buildings[x2]
        gradient = get_gradient(x1,y1,x2,y2)

        if gradient < min_gradient:
            count += 1
            min_gradient = gradient
    
    # right
    max_gradient = -float('inf')
    for x2 in range(x1+1,N):
        y2 = buildings[x2]
        gradient = get_gradient(x1,y1,x2,y2)

        if gradient > max_gradient:
            count += 1
            max_gradient = gradient
    
    answer = max(answer, count)

print(answer)

