'''
N명이 M개의 짐을 나눠서 가져가려고 한다.
가방의 크기는 Bkg이고 1명당 1개의 가방을 멜 수 있다.
짐을 쪼갤 수 없다.
가지고 갈 수 있는 짐의 최대 가치는?
'''

'''
3 10
10
7 1
5 3
4 3
4 2
2 1
8 4
3 2
2 2
1 1
9 7
1: (5,3), (3,2), (2,2)
2: (4,3), (4,2), (2,1)
3: (9,7), (1,1)
answer: 21
'''

import sys
input = sys.stdin.readline

N, B = map(int, input().split())
M = int(input())
loads = [list(map(int, input().split())) for _ in range(M)]

dp = [[[[0] * (B+1) for _ in range(B+1)] for _ in range(B+1)] for _ in range(M+1)]
for i in range(1, M+1):
    w, v = loads[i-1]
    for a in range(B+1):
        for b in range(B+1):
            for c in range(B+1):
                dp[i][a][b][c] = dp[i-1][a][b][c]

                if a >= w:
                    dp[i][a][b][c] = max(dp[i][a][b][c], dp[i-1][a-w][b][c] + v)
                if b >= w:
                    dp[i][a][b][c] = max(dp[i][a][b][c], dp[i-1][a][b-w][c] + v)
                if c >= w:
                    dp[i][a][b][c] = max(dp[i][a][b][c], dp[i-1][a][b][c-w] + v)

print(dp[M][B][B][B])