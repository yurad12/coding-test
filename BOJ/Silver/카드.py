# https://www.acmicpc.net/problem/2164

import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
q = deque(list(range(1,n+1)))

while q:
    if len(q) == 1:
        print(q.popleft())
        break
    q.popleft()
    nx_card = q.popleft()
    q.append(nx_card)