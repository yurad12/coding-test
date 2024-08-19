# https://www.acmicpc.net/problem/16890

import sys
input = sys.stdin.readline
from collections import deque

s1 = list(input().strip())
s2 = list(input().strip())

s1.sort()
s2.sort()

n = len(s1)
if n % 2:
    l = n//2+1
else:
    l = n//2

s1 = deque(s1[:l])
s2 = deque(s2[l:])

answer = ['?'] * n
left, right = 0, n-1

for i in range(n):
    if not i % 2:
        if s1 and (not s2 or s1[0] < s2[-1]):
            answer[left] = s1.popleft()
            left += 1
        else:
            answer[right] = s1.pop()
            right -= 1
    else:
        if s2 and (not s1 or s2[-1] > s1[0]):
            answer[left] = s2.pop()
            left += 1
        else:
            answer[right] = s2.popleft()
            right -= 1

print(''.join(answer))
