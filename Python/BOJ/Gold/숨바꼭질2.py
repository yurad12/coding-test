# https://www.acmicpc.net/problem/12851
import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())

INF = int(1e9)
dp = [[INF, 0] for _ in range(100001)]

q = deque([N])
dp[N][0] = 0
dp[N][1] = 1

while q:
    x = q.popleft()

    for nx in [x+1, x-1, 2*x]:
        if 0 <= nx < 100001:
            if dp[nx][0] > dp[x][0] + 1:
                dp[nx][0] = dp[x][0] + 1
                dp[nx][1] = 1
                q.append(nx)
            elif dp[nx][0] == dp[x][0] + 1:
                dp[nx][1] += 1
                q.append(nx)

print(dp[K][0])
print(dp[K][1])