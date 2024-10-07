# https://www.acmicpc.net/problem/20006

import sys
input = sys.stdin.readline

p, m = map(int, input().split())
players = [map(str.strip, input().split()) for _ in range(p)]

rooms = []
for l, n in players:
    flag = 0
    for i in range(len(rooms)):
        if len(rooms[i]) == m+1:
            continue
        if rooms[i][0]-10 <= int(l) <= rooms[i][0]+10:
            rooms[i].append([int(l),n])
            flag = 1
            break
    if not flag:
        rooms.append([int(l),[int(l),n]])

for room in rooms:
    if len(room) == m+1:
        print("Started!")
    else:
        print("Waiting!")
    
    result = sorted(room[1:], key = lambda x: x[1])
    for l, n in result:
        print(l, n)
