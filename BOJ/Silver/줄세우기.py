# https://www.acmicpc.net/problem/10431

import sys
input = sys.stdin.readline

p = int(input())
for _ in range(p):
    case = list(map(int, input().split()))
    t, heights = case[0], case[1:]

    line, result = [heights[0]], 0

    for h in heights[1:]:
        for i in range(len(line)):
            if line[-1] < h:
                line.append(h)
            elif h < line[i]:
                # 1 2 3 (4) 5 -> 4-2-1
                result += len(line)-i
                line.insert(i,h)
                break
    print("result:",t, result)
