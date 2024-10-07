# https://www.acmicpc.net/problem/2138

import sys
input = sys.stdin.readline

n = int(input())
bulb = list(map(int, input().strip()))
target = list(map(int, input().strip()))
INF = int(1e9)

def switch(bulb, target):
    count = 0
    now = bulb[:]

    # 이전 위치의 상태를 목표로 맞추면서 나아가기
    for i in range(1,n):
        if now[i-1] == target[i-1]: # 목표 상태이기 때문에 동작x
            continue

        for j in range(i-1,i+2):
            if j < n:
                now[j] = not now[j]
        count += 1

    if now == target:
        return count
    else:
        return INF

# case1: 첫 번째 스위치 안 누르는 경우
answer = switch(bulb, target)

# case2: 첫 번째 스위치 누르는 경우
# bulb[0], bulb[1] = 1 - bulb[0], 1 - bulb[1]
bulb[0], bulb[1] = not bulb[0], not bulb[1]
answer = min(answer, switch(bulb, target)+1)

if answer != INF:
    print(answer)
else:
    print(-1)
