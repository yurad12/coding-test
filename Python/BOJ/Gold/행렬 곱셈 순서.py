# https://www.acmicpc.net/problem/11049
'''
2차원 dp

  3 2 6
5 0 30 90
3 0 0 36
2 0 0 0
1. 5로 시작하고 2로 끝나는 행렬(1가지)
    -> 0(5*3) + 0(3*2) + 30(5*3*2) = 30
2. 3으로 시작하고 6으로 끝나는 행렬(1가지)
    -> 0(3*2) + 0(2*6) + 36(3*2*6) = 36
3. 5로 시작하고 6으로 끝나는 행렬(2가지)
    -> 0(5*3) + 36(3*2*6) + 90(5*3*6) = 126
    -> 30(5*2) + 0(2*6) + 60(5*2*6) = 90

min(ABCD) =
    min(
        ABCD,
        min(A) + min(BCD) + (A row * A col * D col)
        min(AB) + min(CD) + (A * B * D)
        min(ABC) + min(D) + (A * C * D) 
    )
'''

import sys
input = sys.stdin.readline

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

INF = float('inf')
dp = [[0] * N for _ in range(N)]

for k in range(1, N): # 간격
    for i in range(N-k):
        dp[i][i+k] = INF

        for j in range(i, i+k):
            dp[i][i+k] = min(dp[i][i+k], dp[i][j] + dp[j+1][i+k] + matrix[i][0]*matrix[j][1]*matrix[i+k][1])

print(dp[0][-1])
