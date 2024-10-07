'''
https://app.codility.com/programmers/lessons/11-sieve_of_eratosthenes/count_non_divisible/


'''

import math

def solution(A):
    n = len(A)
    max_value = max(A)
    
    counts = [0] * (max_value + 1)
    for a in A:
        counts[a] += 1
    
    divisors = [0] * (max_value + 1)
    for i in range(1, int(math.sqrt(max_value)) + 1):
        for j in range(i*i, max_value + 1, i):
            divisors[j] += counts[i]
            if i != j // i:
                divisors[j] += counts[j // i]

    answer = [0] * n
    for i in range(n):
        answer[i] = n - divisors[A[i]]

    return answer