# https://www.acmicpc.net/problem/4095
import sys
input = sys.stdin.readline

while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    mat = [list(map(int, input().split())) for _ in range(N)]

    dp = [[0] * M for _ in range(N)]
    answer = 0

    for i in range(N):
        for j in range(M):
            if mat[i][j]:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                answer = max(answer, dp[i][j])
    
    print(answer)