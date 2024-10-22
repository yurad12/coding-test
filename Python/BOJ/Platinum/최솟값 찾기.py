# https://www.acmicpc.net/problem/11003
import sys
input = sys.stdin.readline
from collections import deque

N, L = map(int, input().split())
A = list(map(int, input().split()))

q = deque()
answer = []
for i in range(N):
    while q and q[-1][0] > A[i]:
        q.pop()
    q.append((A[i], i))
    if q and (q[0][1] <= i-L):
        q.popleft()
    answer.append(q[0][0])

print(*answer)