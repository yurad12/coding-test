# https://www.acmicpc.net/problem/11501
'''
1. 주식 가격이 떨어질 때, 산다.
2. 주식 가격이 올라갈 때, 판다.
'''

import sys
input = sys.stdin.readline

def maximize_profit(n, stock):
    stock.reverse()
    max_value = stock[0]
    result = 0

    for i in range(1,n):
        if max_value < stock[i]:
            max_value = stock[i]
            continue
        result += (max_value - stock[i])
    return result


t = int(input())
for _ in range(t):
    n = int(input())
    stock = list(map(int, input().split()))
    print(maximize_profit(n, stock))