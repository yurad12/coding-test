# https://www.acmicpc.net/problem/2644

import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
a, b = map(int, input().split())
m = int(input())
relations = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    relations[x].append(y)
    relations[y].append(x)

visited = [0] * (n+1)
visited[a] = 1
q = deque([(a,0)])
answer = -1

while q:
    now, count = q.popleft()
    if now == b:
        answer = count
        break

    for i in relations[now]:
        if not visited[i]:
            visited[i] = 1
            q.append((i, count+1))

print(answer)