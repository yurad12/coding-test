# https://www.acmicpc.net/problem/17484
# dp 3차원 배열 -> 방향이 [-1,0,1] 3개니까

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
fuel = [list(map(int, input().split())) for _ in range(n)]
direc = [-1, 0, 1]
INF = int(1e9)

# dp[x][y][d] -> d 방향에서 왔을 때 최소 연료 비용
dp = [[[INF] * 3 for _ in range(m)] for _ in range(n)]

for j in range(m):
    for d in range(3):
        dp[0][j][d] = fuel[0][j]

for i in range(1, n):
    for j in range(m):
        # 이전 방향
        for d in range(3):
            prev_col = j + direc[d]
            if prev_col < 0 or prev_col >= m:
                continue
            # 다음 방향
            for nd in range(3):
                if d == nd:
                    continue
                dp[i][j][nd] = min(dp[i][j][nd], dp[i-1][prev_col][d] + fuel[i][j])

result = INF
for j in range(m):
    for d in range(3):
        result = min(result, dp[n-1][j][d])

print(result)
