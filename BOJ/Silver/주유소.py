'''
oil min = [2, 4, 5]
0 10 10+6 10+6+2 = 18
'''

import sys
input = sys.stdin.readline

n = int(input())
roads = list(map(int, input().split()))
oils = list(map(int, input().split()))

result, cost = 0, int(1e9)
for i in range(n-1):
    cost = min(cost, oils[i])
    result += cost * roads[i]

print(result)