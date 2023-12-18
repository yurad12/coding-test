# https://www.acmicpc.net/problem/10799

import sys
input = sys.stdin.readline

data = input()

stack = []
count = 0

for i in range(len(data)-1):
    if data[i] == '(':
        stack.append('(')
    else:
        stack.pop()
        if data[i-1] == '(':
            count += len(stack)
        else:
            count += 1
print(count)