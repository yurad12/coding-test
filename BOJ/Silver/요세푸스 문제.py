'''
1234567
1: 3 124567
2: 36 12457
3: 362 1457
4: 3627 145
5: 36275 14
6: 362751 4
'''
# 2번씩 회전하면서 젤 앞에있는거 큐에서 빼기

import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
q = deque(list(range(1,n+1)))
print('<', end='')
while q:
    q.rotate(-(k-1))
    print(q.popleft(), end='')

    if len(q) == 0:
        print('>')
    else:
        print(",", end=' ')