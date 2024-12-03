# https://www.acmicpc.net/problem/14891

from collections import deque

gears = [deque(list(map(int,input()))) for _ in range(4)]
k = int(input())
turns = [list(map(int,input().split())) for _ in range(k)]

def rotate_left(gear,direc):
    if gear<0 or gears[gear+1][-2] == gears[gear][2]:
        return
    if gears[gear+1][-2] != gears[gear][2]:
        rotate_left(gear-1,-direc)
        gears[gear].rotate(direc)

def rotate_right(gear,direc):
    if gear>3 or gears[gear-1][2] == gears[gear][-2]:
        return
    if gears[gear-1][2] != gears[gear][-2]:
        rotate_right(gear+1,-direc)
        gears[gear].rotate(direc)

for i in range(k):
    gear, direc = turns[i]
    gear -= 1
    rotate_left(gear-1,-direc)
    rotate_right(gear+1,-direc)
    gears[gear].rotate(direc)

result = 0
i = 1
for gear in gears:
    if gear[0] == 1:
        result += i
    i *= 2
print(result)