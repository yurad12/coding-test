# https://www.acmicpc.net/problem/9935

import sys
input = sys.stdin.readline

s = input().strip()
bomb = input().strip()
n = len(bomb)

stack = []
for ch in s:
    stack.append(ch)

    if ''.join(stack[-n:]) == bomb:
        del stack[-n:]

if stack:
    print(''.join(stack))
else:
    print("FRULA")