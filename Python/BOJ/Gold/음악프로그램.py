# https://www.acmicpc.net/problem/2623
import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
lines = [list(map(int, input().split())) for _ in range(M)]
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)
for i in range(M):
    for j in range(2, lines[i][0]+1):
        a = lines[i][j-1]
        b = lines[i][j]
        graph[a].append(b)
        indegree[b] += 1

q = deque()
for i in range(1, N+1):
    if indegree[i] == 0:
        q.append(i)

answer = []
while q:
    now = q.popleft()
    answer.append(now)

    for i in graph[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)

if len(answer) == N:
    for i in answer:
        print(i)
else:
    print(0)
