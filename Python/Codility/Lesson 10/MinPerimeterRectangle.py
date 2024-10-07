'''
https://app.codility.com/programmers/lessons/10-prime_and_composite_numbers/min_perimeter_rectangle/

- int(1e9) < float(’inf’)
- 시간복잡도: O(sqrt(N))
'''

import math

def solution(N):
    answer = float('inf')

    for i in range(1, int(math.sqrt(N))+1):
        if N % i == 0:
            num1 = i
            num2 = N // i
            perimeter = 2 * (num1 + num2)
            answer = min(answer, perimeter)

    return answer
