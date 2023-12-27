# https://www.acmicpc.net/problem/2800

import sys
input = sys.stdin.readline
from itertools import combinations

s = input()

stack = []
index = []
result = set()

for i in range(len(s)):
    if s[i] == '(':
        stack.append(i)
    elif s[i] == ')':
        index.append((stack.pop(), i))

for i in range(1, len(index)+1):
    temp = list(combinations(index, i))
    for t in temp:
        s2 = list(s)
        for x, y in t:
            s2[x] = ''
            s2[y] = ''
        result.add(''.join(s2).strip())

result = list(result)
result.sort()
for res in result:
    print(res)