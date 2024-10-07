'''
https://app.codility.com/programmers/lessons/10-prime_and_composite_numbers/count_factors/

- 시간복잡도 O(sqrt(N))
- i가 약수면 `answer += 1`
    - 이때, i와 `N // i`가 다르면 `N // i`도 약수
'''

import math

def solution(N):
    answer = 0

    for i in range(1, int(math.sqrt(N))+1):
        if N % i == 0:
            answer += 1
            if i != N // i:
                answer += 1

    return answer