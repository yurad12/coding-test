# https://www.acmicpc.net/problem/12908
import sys
input = sys.stdin.readline
from itertools import permutations

xs, ys = map(int, input().split())
xe, ye = map(int, input().split())
teleport = [] # telpo 6 + end 1
for _ in range(3):
    x1, y1, x2, y2 = map(int, input().split())
    teleport.append((x1,y1,x2,y2))
    teleport.append((x2,y2,x1,y1))
teleport.append((xe,ye,xe,ye))

def get_dist(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)

idx = [i for i in range(7)]
answer = get_dist(xs,ys,xe,ye)
print(teleport)
for perm in permutations(idx):
    print(perm)
    total = 0
    nx, ny = xs, ys
    
    for i in perm:
        x1, y1, x2, y2 = teleport[i][0], teleport[i][1], teleport[i][2], teleport[i][3]
        total += get_dist(nx, ny, x1, y1)
        if x2 == xe and y2 == ye:
            break
        total += 10
        nx, ny = x2, y2
    
    answer = min(answer, total)

print(answer)