# https://www.acmicpc.net/problem/2346

# solution1: 64ms
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
q = deque()
for i in range(n):
    q.append((i+1,nums[i]))

while q:
    now, direc = q.popleft()
    print(now, end=' ')
    if direc < 0:
        direc = -direc
    else:
        direc = -direc + 1
    q.rotate(direc)
print()
