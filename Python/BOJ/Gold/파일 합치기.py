# https://www.acmicpc.net/problem/11066

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    K = int(input())
    files = list(map(int, input().split()))

    # 누적 합 계산
    sum_files = [[0] * K for _ in range(K)]
    for i in range(K):
        sum_files[i][i] = files[i]
        for j in range(i+1, K):
            sum_files[i][j] = sum_files[i][j-1] + files[j]
    
    dp = [[0] * K for _ in range(K)]
    for n in range(2, K+1):
        for i in range(K-n+1):
            j = i + n - 1
            dp[i][j] = int(1e9)
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + sum_files[i][j])

    print(dp[0][K-1])