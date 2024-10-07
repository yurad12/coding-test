# https://www.acmicpc.net/problem/13549

import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())

visited = [0] * (100001)
visited[n] = 1
q = deque([(0,n)])
answer = 100001
while q:
    sec, now = q.popleft()
    if now == k:
        answer = min(answer, sec)

    if now*2 < 100001 and not visited[now*2]:
        q.append((sec,now*2))
        visited[now*2] = 1
    if now-1 >= 0 and not visited[now-1]:
        q.append((sec+1, now-1))
        visited[now-1] = 1
    if now+1 < 100001 and not visited[now+1]:
        q.append((sec+1, now+1))
        visited[now+1] = 1

print(answer)