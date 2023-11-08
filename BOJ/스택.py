# https://www.acmicpc.net/problem/10828
import sys
input = sys.stdin.readline

n = int(input())
# inputList = []
# for _ in range(n):
#     temp = input().split()
#     inputList.append(temp)

stack = []
for _ in range(n):
    temp = input().split()
    if len(temp) == 2:
        stack.append(int(temp[1]))
        continue
    if temp[0] == 'pop':
        if not stack:
            print(-1)
            continue
        num = stack.pop()
        print(num)
    if temp[0] == 'size':
        print(len(stack))
    if temp[0] == 'empty':
        if stack: print(0)
        else: print(1)
    if temp[0] == 'top':
        if not stack:
            print(-1)
            continue
        print(stack[-1])
