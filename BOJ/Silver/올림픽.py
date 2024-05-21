# https://www.acmicpc.net/problem/8979

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
medals = {}
for _ in range(n):
    medal = list(map(int,input().split()))
    medals[medal[0]] = medal[1:]

result = 1
g, s, b = medals[k][0], medals[k][1], medals[k][2]

for key in medals.keys():
    if key == k:
        continue
    
    # 1. 금메달 수가 더 많은 나라
    if medals[key][0] > g:
        result += 1
    # 2. 금메달 수가 같고, 은메달 수가 더 많은 나라
    elif medals[key][0] == g:
        if medals[key][1] > s:
            result += 1
        # 3. 금, 은메달 수가 모두 같고, 동메달 수가 많은 나라
        elif medals[key][1] == s:
            if medals[key][2] > b:
                result += 1

print(result)