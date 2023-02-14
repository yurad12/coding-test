# https://www.acmicpc.net/problem/15483

import sys

a = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()

# 2차원 배열 생성
distance = [[0]*(len(b)+1) for _ in range(len(a)+1)]
for i in range(1,len(a)+1):
    distance[i][0] = i
for j in range(1,len(b)+1):
    distance[0][j] = j

# 거리 계산
# min[f(i,j-1) + ca, f(i-1,j) + cd, f(i-1,j-1) + ct], ca = cd = ct = 1
for i in range(1,len(a)+1):
    for j in range(1,len(b)+1):
        if a[i-1] == b[j-1]:
            distance[i][j] = distance[i-1][j-1]
        else:
            distance[i][j] = min(distance[i][j-1],distance[i-1][j],distance[i-1][j-1]) + 1

print(distance[len(a)][len(b)])
