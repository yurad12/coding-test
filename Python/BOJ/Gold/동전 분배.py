# https://www.acmicpc.net/problem/1943
# knapsack

import sys
input = sys.stdin.readline

def is_possible(n, coins):
    total_coin = sum(coin * count for coin, count in coins)
    if total_coin % 2:
        return 0
    
    target = total_coin // 2

    dp = [0] * 100001
    dp[0] = 1
    for coin, count in coins:
        for now in range(target, coin-1, -1):
            if dp[now-coin]:
                for i in range(count):
                    if now + coin * i > target:
                        break
                    dp[now+coin*i] = 1

    return dp[target]

for _ in range(3):
    N = int(input())
    coins = [list(map(int, input().split())) for _ in range(N)]
    print(is_possible(N, coins))

