# https://www.acmicpc.net/problem/17182
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dist = [list(map(int, input().split())) for _ in range(N)]
INF = float('inf')

for k in range(N):
    for a in range(N):
        for b in range(N):
            dist[a][b] = min(dist[a][b], dist[a][k] + dist[k][b])

dp = [[INF] * N for _ in range(1 << N)]
dp[1<<K][K] = 0

for i in range(1 << N):
    for j in range(N):
        if dp[i][j] == INF:
            continue
        for next in range(N):
            if i & (1 << next) == 0:
                new_path = i | (1 << next)
                dp[new_path][next] = min(dp[new_path][next], dp[i][j] + dist[j][next])

answer = min(dp[(1 << N) - 1][i] for i in range(N))
print(answer)