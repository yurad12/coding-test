# https://www.acmicpc.net/problem/1515

import sys
input = sys.stdin.readline

n = input().strip()

i, result = 0, 0
while True:
    result += 1
    for s in str(result):
        if n[i] == s:
            i += 1
            if i >= len(n):
                print(result)
                exit()

