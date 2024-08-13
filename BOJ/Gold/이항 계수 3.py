# https://www.acmicpc.net/problem/11401
'''
1. 파스칼의 삼각형
C(n,k) = C(n-1,k) + C(n-1,k-1) -> 메모리 초과 or 시간 초과

2. 페르마의 소정리
 - 나눗셈 대신 곱셈 역원을 이용
  -> 시간 복잡도 줄일 수 있음
 - a^(p-1) ≡ 1 (mod p)
  -> a^(p-2) ≡ a^-1 (mod p)
 - C(n,k) mod p = N! * (K!^-1 * (N-K)!^-1) mod p

'''

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
MOD = 1_000_000_007

def get_inversed(x, mod):
    return pow(x, mod-2, mod)

if K == 0 or K == N:
    print(1)
else:
    factorial = [1] * (N+1)
    for i in range(2, N+1):
        factorial[i] = factorial[i-1] * i % MOD
    
    # K!의 역원
    inversed_K = get_inversed(factorial[K], MOD)
    # (N-K)!의 역원
    inversed_NK = get_inversed(factorial[N-K], MOD)

    answer = factorial[N] * inversed_K % MOD * inversed_NK % MOD

    print(answer)
    
