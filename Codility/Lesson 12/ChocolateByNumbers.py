'''
https://app.codility.com/programmers/lessons/12-euclidean_algorithm/chocolates_by_numbers/

- 시간복잡도: O(log(N + M))
- 유클리드 알고리즘
    - 최대 공약수 효율적으로 구하는 방법
    - 두 수 a와 b가 주어졌을 때,
    - a를 b로 나눈 나머지 r을 구함
    - b를 r로 대체하고, r이 0이 될 때까지 이 과정을 반복
    - 이 때의 b가 최대공약수
- (10,4) 0, 4, 8, 2, 6
    - 10, 4 → 4, 2 → 2
    - 10 // 2 = 5
'''

# solution1: math 이용
import math

def solution(N, M):
    gcd = math.gcd(N,M)
    answer = N // gcd

    return answer

# solution2: 직접 구현
def solution(N, M):
    def gcd(a, b):
        if a % b == 0:
            return b
        return gcd(b, a%b)
        
    answer = N // gcd(N,M)

    return answer