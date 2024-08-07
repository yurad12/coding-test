# https://www.acmicpc.net/problem/10830

import sys
input = sys.stdin.readline

N, B = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

def multiply(matA, matB):
    result = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += matA[i][k] * matB[k][j]
            
            result[i][j] %= 1000
    
    return result

# 단위행렬 ->  A*I = A
answer = [[0] * N for _ in range(N)]
for i in range(N):
    answer[i][i] = 1
while B > 0:
    if B % 2:
        answer = multiply(answer, matrix)
    matrix = multiply(matrix, matrix)
    B //= 2
    

for i in range(N):
    print(*answer[i])
