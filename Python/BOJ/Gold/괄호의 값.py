# https://www.acmicpc.net/problem/2504

import sys
input = sys.stdin.readline

bracket = input()

stack = []
result = 0
temp = 1

for i in range(len(bracket)):
    now = bracket[i]

    if now == '(':
        temp *= 2
        stack.append(now)
    elif now == '[':
        temp *= 3
        stack.append(now)
    elif now == ')':
        if not stack or stack[-1] == '[':
            result = 0
            break
        if bracket[i-1] == '(':
            result += temp
        temp //= 2
        stack.pop()
    elif now == ']':
        if not stack or stack[-1] == '(':
            result = 0
            break
        if bracket[i-1] == '[':
            result += temp
        temp //= 3
        stack.pop()

if stack:
    result = 0
print(result)
