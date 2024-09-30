'''
https://www.acmicpc.net/problem/2749
1. 거듭제곱: 재귀 -> 반복, mod 수행x -> o
2. 곱셈: mod 수행 x -> o
'''
import sys
input = sys.stdin.readline

# 행렬 곱셈
def multiply(mat_X, mat_Y, mod):
    mat_XY = [[0]*len(mat_Y[0]) for _ in range(len(mat_X))]

    for i in range(len(mat_X)):
        for j in range(len(mat_Y[0])):
            for k in range(len(mat_X[0])):
                mat_XY[i][j] += (mat_X[i][k] * mat_Y[k][j]) % mod
    
    return mat_XY

# 행렬 거듭제곱
def power(X, n, mod):
    result = [[1,0],[0,1]]

    while n:
        if n % 2 == 1:
            result = multiply(result, X, mod)
        X = multiply(X, X, mod)
        n //= 2

    return result

# 피보나치 수행
def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    mod = 1_000_000
    F = [[1,1],[1,0]]
    fibo = power(F, n-1, mod)
    return fibo[0][0] % mod

n = int(input())
print(fibo(n))