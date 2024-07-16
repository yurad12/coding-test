'''
https://app.codility.com/programmers/lessons/11-sieve_of_eratosthenes/count_semiprimes/

- 시간 복잡도: O(N * log(log(N)) + M)
'''

import math

def solution(N, P, Q):
    arr = [1] * (N+1)
    arr[0], arr[1] = 0, 0
    for i in range(2, int(math.sqrt(N))+1):
        if arr[i]:
            j = 2
            while i * j <= N:
                arr[i*j] = 0
                j += 1

    primes = [i for i in range(2,N+1) if arr[i]]
    
    semi_primes = [0] * (N+1)
    for a in primes:
        for b in primes:
            if a * b > N:
                break
            semi_primes[a*b] = 1

    prefix = [0] * (N+1)
    for i in range(1, N+1):
        prefix[i] = prefix[i-1] + semi_primes[i]


    answer = []
    for i in range(len(P)):
        answer.append(prefix[Q[i]]-prefix[P[i]-1])

    return answer