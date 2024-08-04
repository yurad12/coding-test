# https://www.acmicpc.net/problem/2252

import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
indegree = [0] * (n+1) # in
graph = [[] for _ in range(n+1)] # out
q = deque()
answer = []

for _ in range(m):
    a, b = map(int,input().split())
    indegree[b] += 1
    graph[a].append(b)

for i in range(1,n+1):
    if not indegree[i]:
        q.append(i)

while q:
    now = q.popleft()
    answer.append(now)
    for i in graph[now]:
        indegree[i] -= 1
        if not indegree[i]:
            q.append(i)

print(*answer)

# 1 3 4
# in: 1 1 0
# out: 0 1 1
# indegree가 작은 것부터