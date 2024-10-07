# https://www.acmicpc.net/problem/2579

import sys

n = int(sys.stdin.readline().rstrip())
stairs = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
d = [0] * n

if len(stairs) <= 2:
    print(sum(stairs))
else:
    d[0] = stairs[0]
    d[1] = max(stairs[0] + stairs[1], stairs[1])
    d[2]  = max(stairs[0]+stairs[2], stairs[1]+stairs[2])
    for i in range(3,n):
        d[i] = max(d[i-3]+stairs[i-1]+stairs[i], d[i-2]+stairs[i])
    print(d[n-1])


'''
반례1
10
100
100
1
1
100
100
1
1000
1000
1000

답: 2302
    
    
반례2
3
40
50
60

답: 110

    
반례3
3
30
20
10

답: 40
'''