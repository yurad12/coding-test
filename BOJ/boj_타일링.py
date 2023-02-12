# https://www.acmicpc.net/problem/1793

import sys

# solution 1
answer = []
while True:
    try:
        x = int(sys.stdin.readline())
        d = [1] * 251
        d[1] = 1
        d[2] = 1+2
        for i in range(3,x+1):
            d[i] = d[i-1] + d[i-2]*2
        answer.append(d[x])
    except:
        break
    
for ans in answer:
    print(ans)

# solution 2
x = sys.stdin.readline

def dp(x):
    d = [1] * 251
    d[2] = 1+2
    for i in range(3,x+1):
        d[i] = d[i-1] + d[i-2]*2
    return d[x]

while True:
    try:
        print(dp(int(x())))
    except:
        break