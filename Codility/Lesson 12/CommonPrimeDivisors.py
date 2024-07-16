'''
https://app.codility.com/programmers/lessons/12-euclidean_algorithm/common_prime_divisors/

- 시간복잡도: O(Z * log(max(A) + max(B))**2)
- 1이 나올 때까지 a,b의 최대 공약수로 계속 나눠줌
- 둘 다 1이 나오면, 공통 인수를 갖고 있다는 의미니까 answer += 1
'''

import math

def solution(A, B):
    def divisor(pre_gcd, x):
        while x != 1:
            gcd = math.gcd(pre_gcd, x)
            if gcd == 1:
                return False
            x //= gcd
        return x == 1

    def is_same(a,b):
        gcd_ab = math.gcd(a,b)
        return divisor(gcd_ab, a) and divisor(gcd_ab, b)

    answer = 0
    for a, b in zip(A,B):
        if is_same(a,b):
            answer += 1

    return answer