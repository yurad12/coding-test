# https://www.acmicpc.net/problem/2493
'''
1. 수신 불가능이면 pop
2. 수신 가능하면 result에 인덱스 넣기
'''

import sys
input = sys.stdin.readline

n = int(input())
signals = list(map(int, input().split()))

stack = []
result = [0] * n
for i in range(n):
    while stack:
        if signals[stack[-1][0]] < signals[i]:
            stack.pop()
        else:
            result[i] = stack[-1][0] + 1
            break
    stack.append((i,signals[i]))

print(*result)
