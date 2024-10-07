## 1. 반복 계산
def factorial(n):
    fact = [1] * (n+1)
    for i in range(2, n+1):
        fact[i] = fact[i-1] * i
    return fact

print(factorial(3))
print(factorial(5))

## 2. math 라이브러리
import math

print(math.factorial(3))
print(math.factorial(5))