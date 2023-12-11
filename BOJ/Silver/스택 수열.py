# https://www.acmicpc.net/problem/1874

'''
1~8
만들고 싶은 수열: 4 3 6 8 7 5 2 1
stack: 
operator: + + + + - - + + - + + - - - - -
result: 4 3 6 8 7
'''

import sys
input = sys.stdin.readline

n = int(input())
targets = list(int(input()) for _ in range(n))

now, stack, result = 0, [], []
flag = True

for target in targets:
    while now < target:
        now += 1
        stack.append(now)
        result.append('+')

    if stack[-1] == target:
        stack.pop()
        result.append('-')
    else:
        flag = False
        break

if flag:
   print('\n'.join(result)) 
else:
    print("NO")