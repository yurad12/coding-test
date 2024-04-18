'''
경우1: 첫 번째 집 턴다.
-> 마지막 집 털 수 없다.
경우2: 첫 번째 집 안 턴다.
-> 마지막 집 털 수 있다.
'''

def solution(money):
    answer = 0
    n = len(money)
    
    dp1 = [0] * n
    dp1[0], dp1[1] = money[0], max(money[0], money[1])
    for i in range(2, n-1):
        dp1[i] = max(dp1[i-1], dp1[i-2] + money[i])
    print(dp1)
    
    dp2 = [0] * n
    dp2[0], dp2[1] = 0, money[1]
    for i in range(2, n):
        dp2[i] = max(dp2[i-1], dp2[i-2] + money[i])
    print(dp2)
    
    return max(dp1[-2],dp2[-1])