# https://www.acmicpc.net/problem/2056
import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
infos = [list(map(int, input().split())) for _ in range(N)]

jobs = [[] for _ in range(N+1)]
indegree = [0] * (N+1)
dp = [0] * (N+1)
q = deque()

for i, info in enumerate(infos):
    indegree[i+1] = info[1]
    dp[i+1] = info[0]

    if not info[1]:
        q.append(i+1)
        continue
    for j in info[2:]:
        jobs[j].append(i+1)

while q:
    now = q.popleft()

    for i in jobs[now]:
        dp[i] =  max(dp[i], dp[now] + infos[i-1][0])
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)

print(max(dp))