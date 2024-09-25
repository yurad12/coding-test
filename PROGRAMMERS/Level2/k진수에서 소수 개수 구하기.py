# https://school.programmers.co.kr/learn/courses/30/lessons/92335#

# sol1
import math

def solution(n, k):
    def convert(n, k):
        S = '0123456789'
        converted = ''
        while n > 0:
            converted = S[n%k] + converted
            n //= k
        return converted
    
    def prime_number(n):
        if n == 1:
            return False
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
        return True
    
    converted = convert(n, k)

    s = ''
    answer = 0
    for i, ch in enumerate(converted):
        if ch == '0' and s:
            if prime_number(int(s)):
                answer += 1
            s = ''
        elif ch != '0':
            s += ch
    
    if s and prime_number(int(s)):
        answer += 1
    
    return answer


# sol2
import math

def solution(n, k):
    def convert(n, k):
        converted = ''
        while n > 0:
            converted += str(n%k)
            n //= k
        return converted[::-1]
    
    def prime_number(n):
        if n == 1:
            return False
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
        return True
    
    converted = convert(n, k)
    answer = 0
    for s in converted.split('0'):
        if s and prime_number(int(s)):
            answer += 1
    
    return answer