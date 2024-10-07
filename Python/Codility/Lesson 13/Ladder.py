'''
https://app.codility.com/programmers/lessons/13-fibonacci_numbers/ladder/

- 시간복잡도: O(L)
- 모듈로 연산    
    (a+b)%m=((a%m)+(b%m))%m
'''

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    n, m = max(A), 2 ** max(B)
    fibo = [0] * (n+2)
    fibo[1], fibo[2] = 1, 1
    for i in range(3,n+2):
        fibo[i] = (fibo[i-1] + fibo[i-2]) % m
    
    answer = []
    for a, b in zip(A,B):
        way = fibo[a+1] % (2**b)
        answer.append(way)
    
    return answer