# https://www.acmicpc.net/problem/1270

import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    t = list(map(int, input().split()))

    count, num = 0, None
    for a in t[1:]:
        if count == 0:
            num = a
            count = 1
        elif num == a:
            count += 1
        else:
            count -= 1
    
    count = 0
    for a in t[1:]:
        if num == a:
            count += 1
    
    if t[0]//2 < count:
        print(num)
    else:
        print("SYJKGW")